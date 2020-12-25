def room_num_exists(room, new_number):
    for each in range(0, len(room)):
        if room[each]["num"] == new_number:
            return True
    return False

def load_map(filename="default.map"):
    try:
        file = open(filename, 'r')
    except:
        raise Exception("Could not open {} for reading.".format(filename))
    else:
        room = json.loads(file.read())
        return room
    return []

# RoomNum, RoomName, RoomDescription, North, South, East, West
room_template = {
            "num": -1,
            "name": "",
            "desc": "",
            "n": {"leadsto": -1, "isclosed": False, "islocked": False},
            "s": {"leadsto": -1, "isclosed": False, "islocked": False},
            "e": {"leadsto": -1, "isclosed": False, "islocked": False},
            "w": {"leadsto": -1, "isclosed": False, "islocked": False}}
