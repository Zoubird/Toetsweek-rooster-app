class ConstraintsChecker():
    def __init__(self):
        pass

    def check_language(self, exam, schedule, day, period):
        if exam.subject in ["netl", "entl", "fatl", "dutl", "sptl"]:
            if period == 1:
                return False
            period_before = period - 1
            for test in schedule[day][period_before]["exams"]:
                if test.group_id == exam.group_id:
                    if test.subject in ["netl", "entl", "fatl", "dutl", "sptl"]:
                        return True
        return False


class Helpers():
    def _create_groups(self, data, Group):
        counter = 1
        groups = []
        ch = ["A", "B", "C", "D", "E", "F"]
        for key, val in data.items():
            if "groups" in val:
                for subject, count in val["groups"].items():
                    for k in range(count):
                        grop = Group(group=f"{key}_{subject}_{ch[k]}", id=counter, subjects=[subject])
                        groups.append(grop)
                        counter += 1
            else:
                grop = Group(group=key, id=counter, subjects=list(val.keys()))
                groups.append(grop)
                counter += 1
        return groups

    def _create_exams(self, groups, data, Exam):
        pending_exams = {}
        for group in groups:
            pending_exams[group] = []
            if "_" in group.group:
                # Profile group e.g. '4H_eco_A'
                parts = group.group.split("_")
                duration = data[parts[0]]["sub"][parts[1]]
                exam = Exam(group.group, None, None, parts[1], duration, None, None)  # FIX: group.group not group.id
                pending_exams[group].append(exam)
            else:
                # Whole-class group e.g. '1HA', '4HA'
                for sub in group.subjects:
                    duration = data[group.group][sub]
                    exam = Exam(group.group, None, None, sub, duration, None, None)  # FIX: group.group not group.id
                    pending_exams[group].append(exam)
                pending_exams[group].sort(key=lambda e: -e.duration)
        return pending_exams


def pretty_print_schedule(schedule, all_groups):
    for day, periods in schedule.items():
        print(f"{day}:")
        for period, info in periods.items():
            exams = info["exams"]
            exam_strs = []
            for exam in exams:
                exam_strs.append(f"{exam.subject} (Group {exam.group_id}) (room {exam.room})")
            print(f"  Period {period}: {', '.join(exam_strs) if exam_strs else 'No exams'}")
        print()


def pretty_print_group_counts(group_counts):
    for group, days in group_counts.items():
        print(f"{group}:")
        for day, count in days.items():
            print(f"  {day}: {count} exams")
        print()
