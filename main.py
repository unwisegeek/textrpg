import rooms
import cmds
import art

# Initial Variables
quit_game = False
command = ""
player = { "location": 0
}

# Load the map
room = rooms.load_map("default.map")

def splashscreen():
    art.tprint("SUD", font="impossible")
    print("Welcome to Single User Dungeon...\n\n")
    char_name = input("Please enter your character name: ")
    print("\nWelcome, {}! Now entering the dungeon!")


def exithandler(num, exitdir):
    if room[num][exitdir]["leadsto"] != -1:
        return room[num][exitdir]["leadsto"]
    return -1

splashscreen()

while not quit_game:
    continue_loop = False
    room, player, continue_loop = cmds.handler(room, player, ["look"])

    while not continue_loop:
        command = input("Command: ").lower()

        if command == "":
            continue

        # Command handlers
        if command.split(' ')[0]:
            if command[0] not in "nsew":
                room, player, continue_loop = cmds.handler(room, player, \
                                                           command.split(' '))

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

        if command in "q" or command in "quit" or command in "x":
            continue_loop = True
            quit_game = True
