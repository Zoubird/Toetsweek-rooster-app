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

class ConstraintsChecker():
    def __init__(self):
        pass
