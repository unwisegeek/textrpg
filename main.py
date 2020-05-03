from rooms import room

# Initial Variables
roomnum = 0
keyboardinput = " "


def exithandler(num, exitdir):
    exitvars = {"n": "n-exit", "s": "s-exit", "e": "e-exit", "w": "w-exit"}
    if room[num][exitvars[exitdir]] != -1:
        return room[num][exitvars[exitdir]]
    return -1


while "x" not in keyboardinput.lower():
    # Create exitstr - this is hacky, but I'll make it pretty later.
    exitstr = ""
    if room[roomnum]["n-exit"] != -1:
        exitstr += "n "
    if room[roomnum]["s-exit"] != -1:
        exitstr += "s "
    if room[roomnum]["e-exit"] != -1:
        exitstr += "e "
    if room[roomnum]["w-exit"] != -1:
        exitstr += "w "
    print("{}\n{}\n\nExits: {}\n".format(room[roomnum]['name'], room[roomnum]['desc'], exitstr))
    keyboardinput = input("Command: ")

    # Exit handlers
    if keyboardinput.lower() in "nsew":
        roomnum = exithandler(roomnum, keyboardinput.lower())

