class Scheduler():
    def __init__(self):
        # Available classrooms (these are not all the rooms, more will be included later)
        self.av_rooms = [002, 009, 010, 011, 012, 106, 108, 112, 113, 114, 115, 116, 201, 202, 203, 204, 205]
        # Teacher (more will be added later)
        self.teachers = ["Teacher1", "Teacher2", "Teacher3", "Teacher4", "Teacher5", "Teacher6"]
        self.room_schedule = {
            "Mon": {
                1: [{"room": 002, "class": "3A"}, {"room": 112, "class": "2B"}],
                2: [{"room": 009, "class": "2A"}, {"room": 113, "class": "1B"}],
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
    pass

class Exam():
    def __init__(self,group,day,period,subject,duration,room,supervisor):
        self.group = group
        self.day = day
        self.period = period
        self.subject = subject
        self.duration = duration
        self.room = room
        self.supervisor = supervisor


school = {
  "Year1": {
        "Vwo": {-
            "A": TimeTable(1, 'A'),
            "B": TimeTable(1, 'B'),
            "C": TimeTable(1, 'C') 
        },
        "Havo": 
        {
            "A": TimeTable(1, 'A'),
            "B": TimeTable(1, 'B'),
            "C": TimeTable(1, 'C'),
            "D": TimeTable(1, 'D')
        }
    },
    "Year2": {
        "Vwo": {
            "A": TimeTable(2, 'A'),
            "B": TimeTable(2, 'B'),
            "C": TimeTable(2, 'C')
        },
        "Havo": {
            "A": TimeTable(2, 'A'),
            "B": TimeTable(2, 'B'),
            "C": TimeTable(2, 'C')
        }
    },
    "Year3": {
        "Vwo": {
            "A": TimeTable(3, 'B'),
            "B": TimeTable(3, 'A')
        },
        "Havo": {
            "A": TimeTable(3, 'A'),
            "B": TimeTable(3, 'B'),
            "C": TimeTable(3, 'C')
        }
    }
}
