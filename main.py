from other.helpers import Group, Exam, ConstraintsChecker
from other.vars import classes, schedule
import random, copy

class Scheduler():
    def __init__(self):
        self.lower_classes = []
        self.pending_exams = {}
        self.av_rooms = ["002", "009", "010", "011", "012", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205"]
        self.schedule = copy.deepcopy(schedule)
    
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

    def _place_exam(self, exam, time, room):
        exam.room = room
        exam.day = time[0]
        exam.period = time[1]
        self.schedule[time[0]][time[1]].append(exam)

    def _check_exam(self, pend_exam, lis):
        for exam in lis:
            if pend_exam.group_id == exam.group_id:
                return True
        return False

    def _exams(self):
        for group, pend_exams in self.pending_exams.items():
            for pend_exam in pend_exams:
                room = random.choice(self.av_rooms)
                for day, periods in self.schedule.items():
                    for period, lis in periods.items():
                        if self._check_exam(pend_exam, lis):
                            continue  # conflict, try next period
                        # spot is free, place exam
                        self._place_exam(pend_exam, (day, period), room)
                        break  # stop looping periods for this exam
                    else:
                        continue  # only triggered if inner loop didn't break
                    break  # stop looping days if exam placed
        print(self.schedule)

    def _ext_data_form(self):
        # Later, this function will serve purpose to extract data from the data that has been provided by someone using the algo
        pass

sched = Scheduler()
sched._create_groups()
sched._create_exams()
sched._exams()
