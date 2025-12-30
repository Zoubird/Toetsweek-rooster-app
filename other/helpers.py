class ConstraintsChecker():
    def __init__(self):
        pass

    def check_language(self, exam, schedule, day, period):
        if exam.subject in ["netl", "entl", "fatl", "dutl", "sptl"]:  # If the subject is a language
            if period == 1:
                return False
            period_before = period - 1
            for test in schedule[day][period_before]["exams"]:
                if test.group_id == exam.group_id:
                    if test.subject in ["netl", "entl", "fatl", "dutl", "sptl"]:
                        return True
        return False  # No constraints violated
    
class Helpers():
    def _create_groups(self, classes, Group):
        """Finished, but might add functionality later to use userinput for the amount of classes in vars.classes instead of hardcoded values"""
        counter = 1
        lower_classes = []
        for i in range (1, 4): # Loop 3 times
            for j in ["H", "V"]: # Per loop, go through Havo and Vwo
                for k in range(classes[i][0][j]):
                    ch = ["A", "B", "C", "D", "E", "F"] # Add letter to group
                    # Create group and add to lower_classes
                    lower_classes.append(Group(group=f"{i}{j}{ch[k]}", id=counter, subjects=classes[i][1]))
                    counter += 1
        return lower_classes
    
    def _create_exams(self, lower_classes, data, Exam):
        pending_exams = {}
        for group in lower_classes: # Loops through all groups
            pending_exams[group] = [] # Create a new key-value pair in pending exams with the key as the group
            for sub in group.subjects: # Loops through each subject a group has
                # Create an exam object for the subject and add it to a groups exams in pending_exams
                duration = data[group.group][sub]
                exam = Exam(group.id, None, None, sub, duration, None, None)
                pending_exams[group].append(exam)

                # Sort this group's exams by duration (longest first)
                pending_exams[group].sort(key=lambda exam: -exam.duration)
                
        return pending_exams

def pretty_print_schedule(schedule, low):
    for day, periods in schedule.items():
        print(f"{day}:")
        for period, info in periods.items():
            info = info["exams"]
            exam_strs = []
            for exam in info:
                for i in low:
                    if i.id == exam.group_id:
                        group = i.group
                exam_strs.append(f"{exam.subject} (Group {group})")
            print(f"  Period {period}: {', '.join(exam_strs) if exam_strs else 'No exams'}")
        print()  # blank line between days


def pretty_print_group_counts(group_counts):
    for group, days in group_counts.items():
        print(f"{group}:")
        for day, count in days.items():
            print(f"  {day}: {count} exams")
        print()  # blank line between groups
