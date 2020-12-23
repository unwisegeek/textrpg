from rooms import room
import cmds

# Initial Variables
command = ""
player = { "location": 0
}

def exithandler(num, exitdir):
    if room[num][exitdir]["leadsto"] != -1:
        return room[num][exitdir]["leadsto"]
    return -1

while "x" not in command:
    continue_loop = False
    cmds.dispatcher(room, player, ["look"])

    while not continue_loop:
        command = input("Command: ").lower()

        if command == "":
            continue

        # Command handlers
        if command.split(' ')[0]:
            if command[0] not in "nsew":
                continue_loop = cmds.dispatcher(room, player, command.split(' '))

        # Exit handlers
        if command in "nsew":
            dir_of_travel = command
            new_roomnum = exithandler(player["location"], dir_of_travel)
            # Handle invalid exit
            if new_roomnum == -1:
                print("You cannot go in that direction.")
            # Handle closed doors
            elif room[player["location"]][dir_of_travel]["isclosed"]:
                print("The door is closed.")
            # Set the next room and proceed to the next loop.
            else:
                player["location"] = new_roomnum
                continue_loop = True

        if command in "x":
            continue_loop = True
