from other.helpers import ConstraintsChecker, Helpers, pretty_print_group_counts, pretty_print_schedule
from other.exam import Exam
from other.group import Group
from other.vars import classes, schedule, exams_group, data
import random, copy

class Scheduler():
    def __init__(self):
        # Initiate class variables
        self.MAX_PERIODS = 7
        self.constraint_checker = ConstraintsChecker() # Object to check constraints
        self.helpers = Helpers()
        self.lower_classes = self.helpers._create_groups(classes, Group) # All group objects are stored here from grade 1 to 3
        self.pending_exams = self.helpers._create_exams(self.lower_classes, data, Exam) # All exams that have yet to be planned are stored here per group
        self.schedule = copy.deepcopy(schedule) # The schedule in which exams will be planned in

    def _check_exam(self, pend_exam, lis):
        # Loops through all the exams scheduled at a given period
        for exam in lis:
            if pend_exam.group_id == exam.group_id:
                return True
        # Return False if no conflict found
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
            if not info["rooms"]:  # in case all rooms taken
                continue    

            # Check if it is a multihour exam
            duration = pending_exam.duration
            if duration > 1:
                # Bounds check
                if period + duration - 1 > self.MAX_PERIODS:
                    # Return instead of continuing since the exam can't be placed at all at this day
                    print(f"Couldnt place exam {pending_exam.subject} from {pending_exam.group_id}")
                    return False
                
                # Group conflict check
                conflict = False
                for i in range(period + 1, period + duration):
                    exams = self.schedule[day][i]["exams"]
                    if self._check_exam(pending_exam, exams):
                        conflict = True
                if conflict: continue

                # room continuity check
                room = self.assign_room_to_exam(day, period, pending_exam)
                if room is None: continue
                
                # placement logic if exam passes all checks
                for prd in range(period, period + duration):
                    self._place_exam(pending_exam, day, prd, room)
                exams_p_day[group][day] += 1
                return True

            # last check to see if theres a room available for this exam
            room = self.assign_room_to_exam(day, period, pending_exam)
            if room is None: continue

            self._place_exam(pending_exam, day, period, room)
            exams_p_day[group][day] += 1
            return True  # success
            
        return False  # couldn't place
    
    def _place_exam(self, exam, day, period, room):
        # Assign exam class variables and place it in the schedule
        assert room not in [e.room for e in self.schedule[day][period]["exams"]]
        exam.room = room
        exam.day = day
        exam.period = period
        self.schedule[day][period]["exams"].append(exam)
        print(f"Placed exam {exam.subject} duration {exam.duration} in period {period} with room {exam.room}")
    
    def _loop_through_week(self, exams_per_day, group, pend_exam):
        # Loop through the week
        for day, periods in self.schedule.items():
            # Check if this group already has 2 exams planned on this day
            if exams_per_day[group][day] >= 2:
                continue # Skip to next iteration (day) to loop through
            if self._loop_through_periods(periods=periods, pending_exam=pend_exam, day=day, group=group, exams_p_day=exams_per_day):
                return True

    def exams(self):
        # Tracks exams per day per group
        exams_per_day = {}
        for group in self.pending_exams.keys():
            exams_per_day[group] = copy.deepcopy(exams_group)
        
        # Flatten all exams into one list with their groups
        all_exams = []
        for group, pend_exams in self.pending_exams.items():
            for pend_exam in pend_exams:
                all_exams.append((group, pend_exam))
        
        # Sort by duration (desc), then by group's total exam count (desc)
        all_exams.sort(key=lambda x: (
            -x[1].duration,
            -len(self.pending_exams[x[0]])
        ))
        
        # Place exams in sorted order
        for group, pend_exam in all_exams:
            self._loop_through_week(exams_per_day, group, pend_exam)

        # AI generated these to make the dictionaries readable in terminal
        pretty_print_schedule(self.schedule, self.lower_classes)
        print(self.lower_classes)

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

    def assign_room_to_exam(self, day, period, pending_exam):
        room = self._find_common_room_for_exam(day, period, pending_exam)
        if room is None:
            return None
        pending_exam.room = room
        for i in range(pending_exam.duration):
            self.schedule[day][period+i]["rooms"].remove(room)
        return room

sched = Scheduler()
sched.exams()
