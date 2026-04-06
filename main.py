from other.helpers import ConstraintsChecker, Helpers, pretty_print_group_counts, pretty_print_schedule
from other.exam import Exam
from other.group import Group
from other.vars import classes, schedule, schedule_upper, data
from excelgen import generate_timetable
import copy
# 112,113,114,115,116,117,118,119,120,121,122,123,124,125
# 009,010,011,106,108,112,113,114,115,116
# 201,202,203,204,205
class Scheduler():
    def __init__(self, config):
        self.config = copy.deepcopy(config)
        self.MAX_PERIODS = 7
        self.constraint_checker = ConstraintsChecker()
        self.helpers = Helpers()
        self.all_groups = self.helpers._create_groups(self.config["data"], Group)
        self.pending_exams = self.helpers._create_exams(self.all_groups, self.config["data"], Exam)
        self.schedule = copy.deepcopy(self.config["schedule"])

    def _check_exam(self, pend_exam, lis):
        for exam in lis:
            if pend_exam.group_id == exam.group_id:
                return True
        return False
    
    def _loop_through_periods(self, periods, pending_exam, day, group, exams_p_day):   
        """Loops through the periods of a day for a specific exam"""
        for period, info in periods.items():
            # Language constraint
            if self.constraint_checker.check_language(pending_exam, self.schedule, day, period):
                break

            # Check if theres already an exam of that group in that period
            if self._check_exam(pending_exam, info["exams"]):
                continue 

            # Check if rooms are left
            if not info["rooms"]:
                continue    

            duration = pending_exam.duration
            if duration > 1:
                # 2-hour exams must start at odd periods (1, 3, 5)
                if duration == 2 and period not in [1, 3, 5]:
                    continue

                # Bounds check
                if period + duration - 1 > self.MAX_PERIODS:
                    return False
                
                # Group conflict check
                conflict = False
                for i in range(period + 1, period + duration):
                    exams = self.schedule[day][i]["exams"]
                    if self._check_exam(pending_exam, exams):
                        conflict = True
                if conflict: continue

                # Room continuity check
                room = self._assign_room_to_exam(day, period, pending_exam)
                if room is None: continue
                
                for prd in range(period, period + duration):
                    self._place_exam(pending_exam, day, prd, room)
                exams_p_day[group][day] += 1
                return True

            room = self._assign_room_to_exam(day, period, pending_exam)
            if room is None: continue

            self._place_exam(pending_exam, day, period, room)
            exams_p_day[group][day] += 1
            return True
            
        return False
    
    def _place_exam(self, exam, day, period, room):
        assert room not in [e.room for e in self.schedule[day][period]["exams"]]
        exam.room = room
        exam.day = day
        exam.period = period
        self.schedule[day][period]["exams"].append(exam)
    
    def _loop_through_week(self, exams_per_day, group, pend_exam):
        for day, periods in self.schedule.items():
            if exams_per_day[group][day] >= 2:
                continue
            if self._loop_through_periods(periods=periods, pending_exam=pend_exam, day=day, group=group, exams_p_day=exams_per_day):
                return True
        return False

    def exams(self):        
        # Flatten all exams into one list with their groups
        all_exams = []
        for group, pend_exams in self.pending_exams.items():
            for pend_exam in pend_exams:
                all_exams.append((group, pend_exam))

        # Tracks exams per day per group
        exams_per_day = {}
        for group in self.pending_exams.keys():
            exams_per_day[group] = {day: 0 for day in self.schedule.keys()}

        all_exams.sort(key=lambda x: (
            x[1].subject not in ["netl", "entl", "fatl", "dutl", "sptl"],  # Languages first
            -x[1].duration,
            -len(self.pending_exams[x[0]])
        ))

        failed_exams = []
        for group, pend_exam in all_exams:
            if not self._loop_through_week(exams_per_day, group, pend_exam):
                failed_exams.append((group, pend_exam))
        
        if failed_exams:
            print(f"\n❌ Failed to place {len(failed_exams)} exams:")
            for group, exam in failed_exams:
                print(f"  - {exam.subject} (Group {group.group}, duration {exam.duration})")

        pretty_print_schedule(self.schedule, self.all_groups)

        return self.schedule

    def _find_common_room_for_exam(self, day, period, pending_exam):
        """Search for a room thats available in all consecutive periods"""
        day_schedule = self.schedule[day]
        # Loops for each room in the initial period
        for room in day_schedule[period]["rooms"]:
            conflict = False
            for i in range(pending_exam.duration):
                if room not in day_schedule[period + i]["rooms"]:
                    conflict = True
                    break
            if not conflict:
                return room
        return None

    def _assign_room_to_exam(self, day, period, pending_exam):
        """Assign found room to the exam"""
        # Find a room and return None if no room was found
        room = self._find_common_room_for_exam(day, period, pending_exam)
        if room is None:
            return None
        pending_exam.room = room
        # Remove room from available rooms for each period
        for i in range(pending_exam.duration):
            self.schedule[day][period+i]["rooms"].remove(room)
        return room

class UpperScheduler():
    def __init__(self, config):
        self.config = copy.deepcopy(config)
        self.MAX_PERIODS = config.get("max_periods", 7)
        self.helpers = Helpers()
        self.all_groups = self.helpers._create_groups(self.config["data"], Group)
        self.pending_exams = self.helpers._create_exams(self.all_groups, self.config["data"], Exam)
        self.schedule = copy.deepcopy(self.config["schedule"])
        self.clusters = self.config.get("clusters", {})

    def _get_phase1_subjects(self):
        subjects = set()
        for key, val in self.config["data"].items():
            if "groups" not in val:
                for subject in val.keys():
                    subjects.add(subject)
        return subjects

    def _get_phase2_subjects(self):
        subjects = set()
        for key, val in self.config["data"].items():
            if "groups" in val:
                for subject in val["sub"].keys():
                    subjects.add(subject)

        all_clusters = []
        for grade_clusters in self.clusters.values():
            for cluster in grade_clusters:
                all_clusters.append(cluster)
                for subject in cluster:
                    subjects.discard(subject)

        result = all_clusters + [[s] for s in subjects]
        return result

    def _assign_subjects_to_days(self, phase1_subjects, phase2_subjects):
        days = list(self.schedule.keys())
        day_plan = {day: [] for day in days}
        languages = {"netl", "entl", "fatl", "dutl", "sptl", "en"}

        # Phase 1: one per day sequentially
        for i, subject in enumerate(phase1_subjects):
            day_plan[days[i]].append(subject)

        # Phase 2: spread one per day across all days, cycling if needed
        day_index = 0
        for cluster in phase2_subjects:
            subjects = cluster if isinstance(cluster, list) else [cluster]
            # Find next suitable day
            attempts = 0
            while attempts < len(days):
                day = days[day_index % len(days)]
                if not (any(s in languages for s in subjects) and any(s in languages for s in day_plan[day])):
                    day_plan[day].extend(subjects)
                    day_index += 1
                    break
                day_index += 1
                attempts += 1

        return day_plan
    
    def _find_common_room_for_exam(self, day, period, pending_exam):
        day_schedule = self.schedule[day]
        for room in day_schedule[period]["rooms"]:
            conflict = False
            for i in range(pending_exam.duration):
                if room not in day_schedule[period + i]["rooms"]:
                    conflict = True
                    break
            if not conflict:
                return room
        return None

    def _assign_room_to_exam(self, day, period, pending_exam):
        room = self._find_common_room_for_exam(day, period, pending_exam)
        if room is None:
            return None
        pending_exam.room = room
        for i in range(pending_exam.duration):
            self.schedule[day][period + i]["rooms"].remove(room)
        return room

    def _place_exam(self, exam, day, period, room):
        assert room not in [e.room for e in self.schedule[day][period]["exams"]]
        exam.room = room
        exam.day = day
        exam.period = period
        self.schedule[day][period]["exams"].append(exam)

    def _schedule_day(self, day, subjects):
        to_schedule = []
        for group, exams in self.pending_exams.items():
            for exam in exams:
                if exam.subject in subjects:
                    to_schedule.append((group, exam))

        def sort_key(x):
            group_name = x[0].group
            grade = int(group_name[0])
            level = 1 if "H" in group_name[1] else 2
            return (grade, level)

        to_schedule.sort(key=sort_key)

        for group, exam in to_schedule:
            for period, info in self.schedule[day].items():
                if not info["rooms"]:
                    continue
                room = self._assign_room_to_exam(day, period, exam)
                if room is None:
                    continue
                for prd in range(period, period + exam.duration):
                    self._place_exam(exam, day, prd, room)
                break
            else:
                print(f"❌ Failed to place {exam.subject} (Group {group.group})")

    def exams(self):
        phase1 = self._get_phase1_subjects()
        phase2 = self._get_phase2_subjects()
        print("Phase 1:", phase1)
        print("Phase 2:", phase2)
        day_plan = self._assign_subjects_to_days(phase1, phase2)
        print(day_plan)

        for day, subjects in day_plan.items():
            self._schedule_day(day, subjects)

        pretty_print_schedule(self.schedule, self.all_groups)

        return self.schedule

def get_input():
    print("\n=== Toetsweek Scheduler ===\n")

    # Grades
    raw = input("Grades to schedule (e.g. 1,2,3,4,5,6): ").strip()
    selected_grades = [int(g.strip()) for g in raw.split(",")]

    has_low = any(1 <= n <= 3 for n in selected_grades)
    has_high = any(4 <= n <= 6 for n in selected_grades)

    # Rooms
    rooms_low = []
    rooms_high = []
    if has_low:
        raw = input("Available rooms for lower grades (e.g. 112,113,114): ").strip()
        rooms_low = [r.strip() for r in raw.split(",")]
    if has_high:
        raw = input("Available rooms for upper grades (e.g. 112,113,114): ").strip()
        rooms_high = [r.strip() for r in raw.split(",")]

    # Clusters
    clusters = {}
    if has_high:
        if input("Define clustervakken? (y/n): ").strip().lower() == "y":
            for grade in [g for g in selected_grades if g > 3]:
                grade_clusters = []
                print(f"Grade {grade} clusters, one per line (e.g. bio,nat). Empty line to stop:")
                while True:
                    line = input("  > ").strip()
                    if not line:
                        break
                    grade_clusters.append([s.strip() for s in line.split(",")])
                if grade_clusters:
                    clusters[grade] = grade_clusters

    # Filter data
    selected_data = {k: v for k, v in data.items() if isinstance(k, str) and int(k[0]) in selected_grades}
    selected_classes = {g: classes[g] for g in selected_grades if g in classes}

    return {
        "selected_grades": selected_grades,
        "has_low": has_low,
        "has_high": has_high,
        "rooms_low": rooms_low,
        "rooms_high": rooms_high,
        "clusters": clusters,
        "data": selected_data,
        "classes": selected_classes
    }

if __name__ == '__main__':
    config = get_input()

    if config["has_low"]:
        low_sched = copy.deepcopy(schedule)
        for day in low_sched:
            for _, info in low_sched[day].items():
                info["rooms"] = config["rooms_low"].copy()

        low_config = {
            **config,
            "schedule": low_sched,
            "data": {k: v for k, v in config["data"].items() if int(k[0]) <= 3},
            "classes": {g: config["classes"][g] for g in config["selected_grades"] if g <= 3 and g in config["classes"]}
        }
        
        generate_timetable(Scheduler(config=low_config).exams(), title="Toetsweek rooster FULLY CLAUDE CODED HAHAHEZ",
                        output_path="./timetable.xlsx")

    if config["has_high"]:
        upper_sched = copy.deepcopy(schedule_upper)
        for day in upper_sched:
            for _, info in upper_sched[day].items():
                info["rooms"] = config["rooms_high"].copy()

        high_config = {
            **config,
            "schedule": upper_sched,
            "data": {k: v for k, v in config["data"].items() if int(k[0]) > 3},
            "classes": {g: config["classes"][g] for g in config["selected_grades"] if g > 3 and g in config["classes"]}
        }

        generate_timetable(UpperScheduler(config=high_config).exams(), title="Toetsweek rooster FULLY CLAUDE CODED HAHAHEZ",
                       output_path="./timetable.xlsx")
