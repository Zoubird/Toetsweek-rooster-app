from other.helpers import Group, Exam, ConstraintsChecker, pretty_print_group_counts, pretty_print_schedule
from other.vars import classes, schedule, ex_gr
import random, copy

class Scheduler():
    def __init__(self):
        # Initiate class variables
        self.lower_classes = [] # All group objects are stored here from grade 1 to 3
        self.pending_exams = {} # All exams that have yet to be planned are stored here per group
        # Available rooms
        self.av_rooms = ["002", "009", "010", "011", "012", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205"]
        self.schedule = copy.deepcopy(schedule) # The schedule in which exams will be planned in
    
    def _create_groups(self):
        """Finished, but might add functionality later to use userinput for the amount of classes in vars.classes instead of hardcoded values"""
        counter = 1
        for i in range (1, 4): # Loop 3 times
            for j in ["H", "V"]: # Per loop, go through Havo and Vwo
                for k in range(classes[i][0][j]):
                    ch = ["A", "B", "C", "D", "E", "F"] # Add letter to group
                    self.lower_classes.append(Group(group=f"{i}{j}{ch[k]}", id=counter, subjects=classes[i][1])) # Create group and add to lower_classes
                    counter += 1

    def _create_exams(self):
        for group in self.lower_classes: # Loops through all groups
            self.pending_exams[group] = [] # Create a new key-value pair in pending exams with the key as the group
            for sub in group.subjects: # Loops through each subject a group has
                # Create an exam object for the subject and add it to a groups exams in pending_exams
                exam = Exam(group.id, None, None, sub, None, None, None)
                self.pending_exams[group].append(exam)

    def _place_exam(self, exam, time, room):
        # Assign exam class variables and place it in the schedule
        exam.room = room
        exam.day = time[0]
        exam.period = time[1]
        self.schedule[time[0]][time[1]].append(exam)

    def _check_exam(self, pend_exam, lis):
        # Loops through all the exams scheduled at a given period
        for exam in lis:
            # Returns True if there was a conflict, so there already is an exam from the same group in that period
            if pend_exam.group_id == exam.group_id:
                return True
        # Return False if no conflict found
        return False

    def _exams(self):
        # Tracks exams per day per group
        exams_per_day = {}
        for group, pend_exams in self.pending_exams.items():
            # Adds dict with group and days to exams_per_day
            exams_per_day[group] = copy.deepcopy(ex_gr)
            for pend_exam in pend_exams:
                # Random room
                room = random.choice(self.av_rooms)
                # Loop through the week
                for day, periods in self.schedule.items():
                    # Check if this group already has 2 exams planned on this day
                    if exams_per_day[group][day] >= 2:
                        continue # Skip to next iteration (day) to loop through
                    else: 
                        # Loop through the lesuren
                        for period, lis in periods.items():
                            # Check if theres already an exam of that group in that period
                            if self._check_exam(pend_exam, lis):
                                continue  # conflict, try next period
                            # spot is free, place exam
                            self._place_exam(pend_exam, (day, period), room)
                            exams_per_day[group][day] += 1
                            break  # stop looping periods for this exam
                        else:
                            continue  # only triggered if inner loop didn't break
                    break  # stop looping days if exam placed
        
        # AI generated these to make the dictionaries readable in terminal
        pretty_print_schedule(self.schedule)
        pretty_print_group_counts(exams_per_day)

    def _ext_data_form(self):
        # Later, this function will serve purpose to extract data from the data that has been provided by someone using the algo
        pass

sched = Scheduler()
sched._create_groups()
sched._create_exams()
sched._exams()
