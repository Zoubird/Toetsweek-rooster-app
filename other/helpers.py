class Group():
    def __init__(self,group,id,subjects):
        self.id = id
        self.group = group
        self.subjects = subjects

    def __str__(self):
        return f"Group {self.group}, with ID {self.id}"
    
    def __repr__(self):
        return f"Group {self.group} with ID {self.id}"

class Exam():
    def __init__(self,group_id,day,period,subject,duration,room,supervisor):
        self.group_id = group_id
        self.day = day
        self.period = period
        self.subject = subject
        self.duration = duration
        self.room = room
        self.supervisor = supervisor

    def __repr__(self):
        return f"Exam {self.subject} group {self.group_id}"

class ConstraintsChecker():
    def __init__(self):
        pass

def pretty_print_schedule(schedule):
    for day, periods in schedule.items():
        print(f"{day}:")
        for period, exams in periods.items():
            exam_strs = [f"{exam.subject} (Group {exam.group_id})" for exam in exams]
            print(f"  Period {period}: {', '.join(exam_strs) if exam_strs else 'No exams'}")
        print()  # blank line between days


def pretty_print_group_counts(group_counts):
    for group, days in group_counts.items():
        print(f"{group}:")
        for day, count in days.items():
            print(f"  {day}: {count} exams")
        print()  # blank line between groups
