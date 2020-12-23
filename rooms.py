# RoomNum, RoomName, RoomDescription, North, South, East, West
room = [{
            "num": 0,
            "name": "The Main Room",
            "desc": "This is the first room you will see.",
            "n": {"leadsto":  1, "isclosed": False, "islocked": False},
            "s": {"leadsto": -1, "isclosed": False, "islocked": False},
            "e": {"leadsto": -1, "isclosed": False, "islocked": False},
            "w": {"leadsto": -1, "isclosed": False, "islocked": False}
        },
        {
            "num": 1,
            "name": "The Second Room",
            "desc": "This is the second room you will see.",
            "n": {"leadsto": -1, "isclosed": False, "islocked": False},
            "s": {"leadsto":  0, "isclosed": False, "islocked": False},
            "e": {"leadsto":  2, "isclosed": False, "islocked": False},
            "w": {"leadsto": -1, "isclosed": False, "islocked": False}
        },
        {
            "num": 2,
            "name": "The Third Room",
            "desc": "This is the third room you will see.",
            "n": {"leadsto":  3, "isclosed": False, "islocked": False},
            "s": {"leadsto": -1, "isclosed": False, "islocked": False},
            "e": {"leadsto": -1, "isclosed": False, "islocked": False},
            "w": {"leadsto":  1, "isclosed": False, "islocked": False}
        },
        {
            "num": 3,
            "name": "The Fourth Room",
            "desc": "This is the fourth room you will see.",
            "n": {"leadsto": -1, "isclosed": False, "islocked": False},
            "s": {"leadsto":  2, "isclosed": False, "islocked": False},
            "e": {"leadsto":  4, "isclosed": True, "islocked": True},
            "w": {"leadsto": -1, "isclosed": False, "islocked": False}
        },
        {
            "num": 4,
            "name": "The Fifth Room",
            "desc": "This is the fifth room you will see.",
            "n": {"leadsto": -1, "isclosed": False, "islocked": False},
            "s": {"leadsto": -1, "isclosed": False, "islocked": False},
            "e": {"leadsto": -1, "isclosed": False, "islocked": False},
            "w": {"leadsto":  3, "isclosed": False, "islocked": False}
        },
]
