classes = {
    1: [{"H": 4, "V": 3}, ["netl", "entl", "fatl", "sptl", "ges", "bio", "ak", "wis"]],
    2: [{"H": 3, "V": 3}, ["netl", "entl", "fatl", "dutl", "sptl", "ges", "bio", "ak", "nask", "wis"]],
    3: [{"H": 3, "V": 2}, ["netl", "entl", "fatl", "dutl", "sptl", "eco", "ges", "nat", "sch", "wis"]]
}
data = {'1HA': {'netl': 2, 'entl': 3, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 2, 'ak': 1, 'wis': 3},
        '1HB': {'netl': 2, 'entl': 2, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 2, 'ak': 2, 'wis': 2},
        '1HC': {'netl': 2, 'entl': 1, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'wis': 1},
        '1HD': {'netl': 1, 'entl': 1, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'wis': 1},
        '1VA': {'netl': 1, 'entl': 1, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'wis': 1},
        '1VB': {'netl': 1, 'entl': 1, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'wis': 2},
        '1VC': {'netl': 1, 'entl': 1, 'fatl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'wis': 2},
        '2HA': {'netl': 2, 'entl': 1, 'fatl': 1, 'dutl': 1, 'sptl': 1, 'ges': 1, 'bio': 2, 'ak': 1, 'nask': 1, 'wis': 2},
        '2HB': {'netl': 2, 'entl': 2, 'fatl': 2, 'dutl': 2, 'sptl': 2, 'ges': 2, 'bio': 2, 'ak': 1, 'nask': 1, 'wis': 2},
        '2HC': {'netl': 1, 'entl': 1, 'fatl': 1, 'dutl': 1, 'sptl': 1, 'ges': 2, 'bio': 2, 'ak': 1, 'nask': 1, 'wis': 1},
        '2VA': {'netl': 1, 'entl': 1, 'fatl': 1, 'dutl': 1, 'sptl': 1, 'ges': 1, 'bio': 1, 'ak': 1, 'nask': 1, 'wis': 1},
        '2VB': {'netl': 2, 'entl': 2, 'fatl': 2, 'dutl': 2, 'sptl': 2, 'ges': 2, 'bio': 2, 'ak': 2, 'nask': 3, 'wis': 3},
        '2VC': {'netl': 1, 'entl': 1, 'fatl': 1, 'dutl': 1, 'sptl': 2, 'ges': 2, 'bio': 2, 'ak': 2, 'nask': 2, 'wis': 2},
        '3HA': {'netl': 1, 'entl': 1, 'fatl': 1, 'dutl': 1, 'sptl': 1, 'eco': 1, 'ges': 2, 'nat': 2, 'sch': 2, 'wis': 2},
        '3HB': {'netl': 2, 'entl': 2, 'fatl': 2, 'dutl': 2, 'sptl': 2, 'eco': 2, 'ges': 2, 'nat': 2, 'sch': 2, 'wis': 2},
        '3HC': {'netl': 2, 'entl': 2, 'fatl': 2, 'dutl': 2, 'sptl': 2, 'eco': 2, 'ges': 2, 'nat': 2, 'sch': 2, 'wis': 2},
        '3VA': {'netl': 2, 'entl': 2, 'fatl': 2, 'dutl': 2, 'sptl': 2, 'eco': 2, 'ges': 2, 'nat': 2, 'sch': 2, 'wis': 3},
        '3VB': {'netl': 3, 'entl': 3, 'fatl': 3, 'dutl': 3, 'sptl': 3, 'eco': 3, 'ges': 3, 'nat': 3, 'sch': 3, 'wis': 3}
}

schedule = {
    "Mon": {
        1: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        2: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        3: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        4: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        5: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        6: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        7: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]}
    },
    "Tu": {
        1: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        2: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        3: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        4: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        5: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        6: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        7: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]}
    },
    "Wed": {
        1: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        2: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        3: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        4: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        5: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        6: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        7: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]}
    },
    "Thu": {
        1: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        2: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        3: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        4: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        5: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        6: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        7: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]}
    },
    "Fri": {
        1: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        2: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        3: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        4: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        5: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        6: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]},
        7: {"exams": [], "rooms": ["009", "010", "011", "106", "108", "112", "113", "114", "115", "116", "201", "202", "203", "204", "205", "302", "311"], "av_sup": ["Lak", "Mzw", "Ver", "Eau", "Dga", "Kea", "Ero", "Sko", "Cpl", "Hkl", "Wru", "Bce", "Bho", "Qbi", "Sig", "Bdb", "Bgm", "Ewe", "Jli", "Ozs", "Met", "Wgu", "Erh"]}
    }
}

exams_group = {"Mon": 0, "Tu": 0, "Wed": 0, "Thu": 0, "Fri": 0}


