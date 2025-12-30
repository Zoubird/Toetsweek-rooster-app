class Group():
    def __init__(self,group,id,subjects):
        self.id = id
        self.group = group
        self.subjects = subjects

    def __str__(self):
        return f"Group {self.group}, with ID {self.id}"
    
    def __repr__(self):
        return f"Group {self.group} with ID {self.id}"
