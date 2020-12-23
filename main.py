from rooms import room
import cmds

# Initial Variables
roomnum = 0
keyboardinput = " "
global room


def exithandler(num, exitdir):
    if room[num][exitdir]["leadsto"] != -1:
        return room[num][exitdir]["leadsto"]
    return -1


while "x" not in keyboardinput.lower():
    continue_loop = False
    cmds.look(room, roomnum)

    while not continue_loop:
        keyboardinput = input("Command: ")

        if keyboardinput.lower() == "":
            continue

        # Exit handlers
        if keyboardinput.lower() in "nsew":
            dir_of_travel = keyboardinput.lower()
            new_roomnum = exithandler(roomnum, dir_of_travel)
            # Handle invalid exit
            if new_roomnum == -1:
                print("You cannot go in that direction.")
            # Handle closed doors
            elif room[roomnum][dir_of_travel]["isclosed"]:
                print("The door is closed.")
            # Set the next room and proceed to the next loop.
            else:
                roomnum = new_roomnum
                continue_loop = True

        if keyboardinput.lower() in "x":
            continue_loop = True
