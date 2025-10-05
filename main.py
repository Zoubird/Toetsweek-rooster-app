from other.helpers import Group, Exam, ConstraintsChecker
from other.vars import classes
import random

class Scheduler():
    def __init__(self):
        self.lower_classes = []
        self.pending_exams = {}
        self.av_rooms = ["002", "009", "010", "011", "012", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205"]
        self.room_schedule = {
            "Mon": {
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: []
            },
            "Tu": {
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: []
            },
            "Wed": {
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: []
            },
            "Thu": {
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: []
            },
            "Fri": {
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: []
            }
        }
    
    def _create_groups(self):
        """Finished, but might add functionality later to use userinput for the amount of classes in vars.classes instead of hardcoded values"""
        counter = 1
        for i in range (1, 4):
            for j in ["H", "V"]:
                for k in range(classes[i][0][j]):
                    ch = ["A", "B", "C", "D", "E", "F"]
                    self.lower_classes.append(Group(group=f"{i}{j}{ch[k]}", id=counter, subjects=classes[i][1]))
                    counter += 1

    def _create_exams(self):
        for group in self.lower_classes:
            self.pending_exams[group] = []
            for sub in group.subjects:
                exam = Exam(group.id, None, None, sub, None, None, None)
                self.pending_exams[group].append(exam)

    def _place_exam(self):
        pass

    def _ext_data_form(self):
        # Later, this function will serve purpose to extract data from the data that has been provided by someone using the algo
        pass

sched = Scheduler()
sched._create_groups()
sched._create_exams()
