xclasses = {
    1: {"levels": {"H": 4, "V": 3}, "subjects": ["netl", "en", "fatl", "sptl", "ges", "bio", "ak", "wis"]},
    2: {"levels": {"H": 3, "V": 3}, "subjects": ["netl", "en", "fatl", "du", "sptl", "ges", "bio", "ak", "nask", "wis"]},
    3: {"levels": {"H": 3, "V": 2}, "subjects": ["netl", "en", "fatl", "du", "bio", "fi", "eco", "ges", "nat", "sk", "wis"]}
}

classes = {
    1: {"H": {"count": 4, "subjects": ["netl", "en", "fatl", "sptl", "ges", "bio", "ak", "wis"]},
        "V": {"count": 3, "subjects": ["netl", "en", "fatl", "sptl", "ges", "bio", "ak", "wis"]}},
    2: {"H": {"count": 3, "subjects": ["netl", "en", "fatl", "du", "sptl", "ges", "bio", "ak", "nask", "wis"]},
        "V": {"count": 3, "subjects": ["netl", "en", "fatl", "du", "sptl", "ges", "bio", "ak", "nask", "wis"]}},
    3: {"H": {"count": 3, "subjects": ["netl", "en", "fatl", "du", "bio", "eco", "nat", "sk", "wis"]},
        "V": {"count": 2, "subjects": ["netl", "en", "fatl", "du", "bio", "fi", "eco", "nat", "sk", "wis"]}}
}

data_lower = {
    '1HA': {'netl': 2, 'en': 3, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 2, 'ak': 1, 'wis': 3},
    '1HB': {'netl': 2, 'en': 2, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 2, 'ak': 2, 'wis': 2},
    '1HC': {'netl': 2, 'en': 1, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'wis': 1},
    '1HD': {'netl': 1, 'en': 1, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'wis': 1},
    '1VA': {'netl': 1, 'en': 1, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'wis': 1},
    '1VB': {'netl': 1, 'en': 1, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'wis': 2},
    '1VC': {'netl': 1, 'en': 1, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'wis': 2},
    '2HA': {'netl': 2, 'en': 1, 'fatl': 1, 'du': 1, 'sptl': 1, 'ges': 1, 'bio': 2, 'ak': 1, 'nask': 1, 'wis': 2},
    '2HB': {'netl': 2, 'en': 2, 'fatl': 2, 'du': 2, 'sptl': 2, 'ges': 2, 'bio': 2, 'ak': 1, 'nask': 1, 'wis': 2},
    '2HC': {'netl': 1, 'en': 1, 'fatl': 1, 'du': 1, 'sptl': 1, 'ges': 2, 'bio': 2, 'ak': 1, 'nask': 1, 'wis': 1},
    '2VA': {'netl': 1, 'en': 1, 'fatl': 1, 'du': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'nask': 1, 'wis': 1},
    '2VB': {'netl': 2, 'en': 2, 'fatl': 2, 'du': 2, 'sptl': 2, 'ges': 2, 'bio': 2, 'ak': 2, 'nask': 3, 'wis': 3},
    '2VC': {'netl': 1, 'en': 1, 'fatl': 1, 'du': 1, 'sptl': 2, 'ges': 2, 'bio': 2, 'ak': 2, 'nask': 2, 'wis': 2},
    '3HA': {"sk": 1, "du": 1, "en": 2, 'nat': 1, 'bio': 2, 'netl': 1, 'eco': 1, 'wis': 1, 'fatl': 1},
    '3HB': {"sk": 1, "du": 1, "en": 2, 'nat': 1, 'bio': 2, 'netl': 1, 'eco': 1, 'wis': 1, 'fatl': 1},
    '3HC': {"sk": 1, "du": 1, "en": 2, 'nat': 1, 'bio': 2, 'netl': 1, 'eco': 1, 'wis': 1, 'fatl': 1},
    '3VA': {"sk": 1, "du": 1, "en": 1, "nat": 1, "bio": 2, "netl": 1, "fatl": 1, "fi": 1, "eco": 1, "wis": 1},
    '3VB': {"sk": 1, "du": 1, "en": 1, "nat": 1, "bio": 2, "netl": 1, "fatl": 1, "fi": 1, "eco": 1, "wis": 1},
}

data_upper = {
        '4HA': {"netl": 3, "en": 1, "maat": 1},
        '4HB': {"netl": 3, "en": 1, "maat": 1},
        '4HC': {"netl": 3, "en": 1, "maat": 1},
        '4H': {
            "groups": {"eco": 2, "wisA": 2, "wisB": 1, "sk": 2, "nlt": 1, "nat": 1, "ges": 2, "bio": 2}, # Groups per subject
            "sub": {"eco": 2, "wisA": 2, "wisB": 2, "sk": 1, "nlt": 2, "nat": 1, "ges": 1, "bio": 2} # Duration of each subject
        },
        '4VA': {"netl": 3, "maat": 1, "entl": 1},
        '4VB': {"netl": 3, "maat": 1, "entl": 1},
        '4V': {
            "groups": {"eco": 2, "wisA": 2, "wisB": 1, "beco": 1, "sk": 1, "nat": 1, "fatl": 1, "dutl": 1}, # Groups per subject
            "sub": {"eco": 2, "wisA": 2, "wisB": 2, "beco": 2, "sk": 1, "nat": 1, "fatl": 1, "dutl": 1} # Duration of each subject
        },
        '5HA': {"netl": 3, "en": 1},
        '5HB': {"netl": 3, "en": 1},
        '5H': {
            "groups": {"eco": 1, "nat": 1, "ges": 1, "sk": 1, "wisA": 1, "wisB": 1, "beco": 1, "bio": 1, "fatl": 1, "dutl": 1}, # Groups per subject
            "sub": {"eco": 2, "nat": 2, "ges": 2, "sk": 2, "wisA": 3, "wisB": 3, "beco": 2, "bio": 2, "fatl": 1, "dutl": 1} # Duration of each subject
        },
        '5VA': {"netl": 3, "entl": 1},
        '5VB': {"netl": 3, "entl": 1},
        '5V': {
            "groups": {"wisA": 1, "wisB": 1, "ges": 1, "sk": 1, "nat": 1, "eco": 1, "bio": 1, "beco": 1, "fatl": 1, "dutl": 1}, # Groups per subject
            "sub": {"wisA": 3, "wisB": 3, "ges": 2, "sk": 1, "nat": 2, "eco": 2, "bio": 2, "beco": 2, "fatl": 1, "dutl": 1} # Duration of each subject
        },
        '6VA': {"netl": 3, "en": 1},
        '6VB': {"netl": 3, "en": 1},
        '6V': {
            "groups": {"wisA": 1, "wisB": 1, "bio": 1, "eco": 1, "sk": 1, "beco": 1, "nat": 1, "ges": 1, "dutl": 1, "fatl": 1}, # Groups per subject
            "sub": {"wisA": 3, "wisB": 3, "bio": 3, "eco": 2, "sk": 2, "beco": 3, "nat": 2, "ges": 2, "dutl": 1, "fatl": 1} # Duration of each subject
        },
}

data = {**data_lower, **data_upper}

schedule = {
    "Mon": {
        1: {"exams": [], "rooms": []},
        2: {"exams": [], "rooms": []},
        3: {"exams": [], "rooms": []},
        4: {"exams": [], "rooms": []},
        5: {"exams": [], "rooms": []},
        6: {"exams": [], "rooms": []},
        7: {"exams": [], "rooms": []}
    },
    "Tu": {
        1: {"exams": [], "rooms": []},
        2: {"exams": [], "rooms": []},
        3: {"exams": [], "rooms": []},
        4: {"exams": [], "rooms": []},
        5: {"exams": [], "rooms": []},
        6: {"exams": [], "rooms": []},
        7: {"exams": [], "rooms": []}
    },
    "Wed": {
        1: {"exams": [], "rooms": []},
        2: {"exams": [], "rooms": []},
        3: {"exams": [], "rooms": []},
        4: {"exams": [], "rooms": []},
        5: {"exams": [], "rooms": []},
        6: {"exams": [], "rooms": []},
        7: {"exams": [], "rooms": []}
    },
    "Thu": {
        1: {"exams": [], "rooms": []},
        2: {"exams": [], "rooms": []},
        3: {"exams": [], "rooms": []},
        4: {"exams": [], "rooms": []},
        5: {"exams": [], "rooms": []},
        6: {"exams": [], "rooms": []},
        7: {"exams": [], "rooms": []}
    },
    "Fri": {
        1: {"exams": [], "rooms": []},
        2: {"exams": [], "rooms": []},
        3: {"exams": [], "rooms": []},
        4: {"exams": [], "rooms": []},
        5: {"exams": [], "rooms": []},
        6: {"exams": [], "rooms": []},
        7: {"exams": [], "rooms": []}
    }
}

schedule_upper = {
    "Mon": {p: {"exams": [], "rooms": []} for p in range(1, 8)},
    "Tu":  {p: {"exams": [], "rooms": []} for p in range(1, 8)},
    "Wed": {p: {"exams": [], "rooms": []} for p in range(1, 8)},
    "Thu": {p: {"exams": [], "rooms": []} for p in range(1, 8)},
    "Fri": {p: {"exams": [], "rooms": []} for p in range(1, 8)},
    "Sat": {p: {"exams": [], "rooms": []} for p in range(1, 8)},
    "Sun": {p: {"exams": [], "rooms": []} for p in range(1, 8)},
}

exams_group = {"Mon": 0, "Tu": 0, "Wed": 0, "Thu": 0, "Fri": 0}


