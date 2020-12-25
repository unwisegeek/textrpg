import rooms
import cmds
import art
import yaml

# Initial Variables
quit_game = False
command = ""
player = { "location": 0
}

# Load the Config
config = yaml.safe_load(open("textrpg.conf", "r").read())

# Load the map
room = rooms.load_map(config["game"]["map"])

def splashscreen(config):
    # Get strings from Config
    splash = config["game"]["splash"]
    gamename = config["game"]["title"]
    art.tprint(splash, font="impossible")
    print("Welcome to {}...\n\n".format(gamename))
    char_name = input("Please enter your character name: ")
    print("\nWelcome, {}! Now entering the dungeon!")


def exithandler(num, exitdir):
    if room[num][exitdir]["leadsto"] != -1:
        return room[num][exitdir]["leadsto"]
    return -1

splashscreen(config)

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
