from rooms import room

# Initial Variables
roomnum = 0
keyboardinput = " "


def exithandler(num, exitdir):
    if room[num][exitdir]] != -1:
        return room[num][exitvars[exitdir]]
    return -1


while "x" not in keyboardinput.lower():
    # Create exitstr - this is hacky, but I'll make it pretty later.
    exitstr = ""
    exit_list = ["n", "s", "e", "w"]
    for exit in exit_list:
        if room[roomnum][exit] != -1:
            exitstr += "{} ".format(exit)

    print("{}\n{}\n\nExits: {}\n".format(room[roomnum]['name'], room[roomnum]['desc'], exitstr))
    keyboardinput = input("Command: ")

    # Exit handlers
    if keyboardinput.lower() in "nsew":
        roomnum = exithandler(roomnum, keyboardinput.lower())
