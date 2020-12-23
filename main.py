from rooms import room

# Initial Variables
roomnum = 0
keyboardinput = " "


def exithandler(num, exitdir):
    if room[num][exitdir]["leadsto"] != -1:
        return room[num][exitdir]["leadsto"]
    return -1


while "x" not in keyboardinput.lower():
    # Create exitstr - this is hacky, but I'll make it pretty later.
    exitstr = ""
    exit_list = ["n", "s", "e", "w"]
    for exit in exit_list:
        if room[roomnum][exit]["leadsto"] != -1:
            if room[roomnum][exit]["islocked"]:
                exitstr += "<{}> ".format(exit)
            else:
                exitstr += "{} ".format(exit)

    print("{}\n{}\n\nExits: {}\n".format(room[roomnum]['name'],
                                         room[roomnum]['desc'],
                                         exitstr))
    keyboardinput = input("Command: ")

    # Exit handlers
    if keyboardinput.lower() in "nsew":
        new_roomnum = exithandler(roomnum, keyboardinput.lower())
        if new_roomnum == -1:
            print("You cannot go in that direction.")
        else:
            roomnum = new_roomnum
