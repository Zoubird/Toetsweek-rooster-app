from other.helpers import Group, Exam, ConstraintsChecker, pretty_print_group_counts, pretty_print_schedule
from other.vars import classes, schedule, ex_gr
import random, copy

class Scheduler():
    def __init__(self):
        # Initiate class variables
        self.constraint_checker = ConstraintsChecker() # Object to check constraints
        self.lower_classes = [] # All group objects are stored here from grade 1 to 3
        self.pending_exams = {} # All exams that have yet to be planned are stored here per group
        self.schedule = copy.deepcopy(schedule) # The schedule in which exams will be planned in
    
    def _create_groups(self):
        """Finished, but might add functionality later to use userinput for the amount of classes in vars.classes instead of hardcoded values"""
        counter = 1
        for i in range (1, 4): # Loop 3 times
            for j in ["H", "V"]: # Per loop, go through Havo and Vwo
                for k in range(classes[i][0][j]):
                    ch = ["A", "B", "C", "D", "E", "F"] # Add letter to group
                    # Create group and add to lower_classes
                    self.lower_classes.append(Group(group=f"{i}{j}{ch[k]}", id=counter, subjects=classes[i][1]))
                    counter += 1

    def _create_exams(self):
        for group in self.lower_classes: # Loops through all groups
            self.pending_exams[group] = [] # Create a new key-value pair in pending exams with the key as the group
            for sub in group.subjects: # Loops through each subject a group has
                # Create an exam object for the subject and add it to a groups exams in pending_exams
                exam = Exam(group.id, None, None, sub, None, None, None)
                self.pending_exams[group].append(exam)

    def _place_exam(self, exam, day, period, room):
        # Assign exam class variables and place it in the schedule
        exam.room = room
        exam.day = day
        exam.period = period
        self.schedule[day][period]["exams"].append(exam)

    def _check_exam(self, pend_exam, lis):
        # Loops through all the exams scheduled at a given period
        for exam in lis:
            # Returns True if there was a conflict, so there already is an exam from the same group in that period
            if pend_exam.group_id == exam.group_id:
                return True
        # Return False if no conflict found
        return False

    def _loop_periods(self, periods, pending_exam, day, group, exams_p_day):
        """Loops through the periods of a day for a specific exam"""
        # Loop through the periods
        for period, info in periods.items():
            if self.constraint_checker.check_language(pending_exam, self.schedule, day, period):
                break
            # Check if theres already an exam of that group in that period
            if self._check_exam(pending_exam, info["exams"]):
                continue  # conflict, try next period
            if not info["rooms"]:  # in case all rooms taken
                continue
            # spot is free, place exam
            room = random.choice(info["rooms"])
            self._place_exam(pending_exam, day, period, room)
            info["rooms"].remove(room)
            exams_p_day[group][day] += 1
            return True  # success
        return False  # couldn't place

    def _exams(self):
        # Tracks exams per day per group
        exams_per_day = {}
        for group, pend_exams in self.pending_exams.items():
            # Adds dict with group and days to exams_per_day
            exams_per_day[group] = copy.deepcopy(ex_gr)
            for pend_exam in pend_exams:
                # Loop through the week
                for day, periods in self.schedule.items():
                    # Check if this group already has 2 exams planned on this day
                    if exams_per_day[group][day] >= 2:
                        continue # Skip to next iteration (day) to loop through
                    if self._loop_periods(periods=periods, pending_exam=pend_exam, day=day, group=group, exams_p_day=exams_per_day):
                        break
        
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
