class Scheduler():
    def __init__(self):
        # Available classrooms (these are not all the rooms, more will be included later)
        self.av_rooms = [002, 009, 010, 011, 012, 106, 108, 112, 113, 114, 115, 116, 201, 202, 203, 204, 205]
        # Teacher (more will be added later)
        self.teachers = ["Teacher1", "Teacher2", "Teacher3", "Teacher4", "Teacher5", "Teacher6"]
        self.room_schedule = {
            "Mon": {
                1: [{"room": 002, "class": "3A"}, {"room": 112, "class": "2B"}],
                2: [{"room": 009, "class": "2A"}, {"room": 1123, "class": "1B"}],
                3: [],
                4: [],
                5: [],
                6: [],
                7: []}}
        self.teacher_schedule = {}

    def _ext_data_form(self):
        # Later, this function will serve purpose to extract data from the data that has been provided by someone using the algo
        pass

class TimeTable():
    def __init__(self, year, letter):
        self.year = year
        self.letter = letter
        self.timetable = {
            "Mon": {
                    1: {"sub": None, "teach": None, "room": None},
                    2: {"sub": None, "teach": None, "room": None},
                    3: {"sub": None, "teach": None, "room": None},
                    4: {"sub": None, "teach": None, "room": None},
                    5: {"sub": None, "teach": None, "room": None},
                    6: {"sub": None, "teach": None, "room": None},
                    7: {"sub": None, "teach": None, "room": None}},
            "Tue": {
                    1: {"sub": None, "teach": None, "room": None},
                    2: {"sub": None, "teach": None, "room": None},
                    3: {"sub": None, "teach": None, "room": None},
                    4: {"sub": None, "teach": None, "room": None},
                    5: {"sub": None, "teach": None, "room": None},
                    6: {"sub": None, "teach": None, "room": None},
                    7: {"sub": None, "teach": None, "room": None}},
            "Wed": {
                    1: {"sub": None, "teach": None, "room": None},
                    2: {"sub": None, "teach": None, "room": None},
                    3: {"sub": None, "teach": None, "room": None},
                    4: {"sub": None, "teach": None, "room": None},
                    5: {"sub": None, "teach": None, "room": None},
                    6: {"sub": None, "teach": None, "room": None},
                    7: {"sub": None, "teach": None, "room": None}},
            "Thu": {
                    1: {"sub": None, "teach": None, "room": None},
                    2: {"sub": None, "teach": None, "room": None},
                    3: {"sub": None, "teach": None, "room": None},
                    4: {"sub": None, "teach": None, "room": None},
                    5: {"sub": None, "teach": None, "room": None},
                    6: {"sub": None, "teach": None, "room": None},
                    7: {"sub": None, "teach": None, "room": None}},
            "Fri": {
                    1: {"sub": None, "teach": None, "room": None},
                    2: {"sub": None, "teach": None, "room": None},
                    3: {"sub": None, "teach": None, "room": None},
                    4: {"sub": None, "teach": None, "room": None}, 
                    5: {"sub": None, "teach": None, "room": None},
                    6: {"sub": None, "teach": None, "room": None},
                    7: {"sub": None, "teach": None, "room": None}}
        }

    def place_subject(self, day, period, lecture):
        # Check for necessary variables (will be removed later and checked elsewhere)
        assert day
        assert period
        assert lecture
        if self.timetable[day][period]["sub"] is None:
            if self._check_prof_sub(day, period):
                if self._check_languages(day, period):
                    self._alter_timetable(day, period, lecture)

    
    def _check_languages(self, day, period):
        # Two languages cannot be back-to-back
        pass
    
    def _check_prof_sub(self, day, period):
        # Two profilesubject cannot be back-to-back
        pass

    def _alter_timetable(self, day, period, lecture):
        # Schedule a subject at the desired period
        self.timetable[day][period] = lecture


school = {
  "Year1": {
    "ClassA": TimeTable(1, 'A'),
    "ClassB": TimeTable(1, 'B'),
    "ClassC": TimeTable(1, 'C')
  },
  "Year2": {
    "ClassA": TimeTable(2, 'A'),
    "ClassB": TimeTable(2, 'B'),
    "ClassC": TimeTable(2, 'C')
  },
  "Year3": {
    "ClassA": TimeTable(3, 'A'),
    "ClassB": TimeTable(3, 'B'),
    "ClassC": TimeTable(3, 'C')
  }
}
