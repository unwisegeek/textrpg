# All possible player commands must fall under the handler function.
# Returns room, player, and True or False depending on if main loop should
# continue (True) or wait for additional player input (False).
def handler(room, player, command):

    def look(room, player, args):
        # Show the room name, description, and exits to players.
        roomnum = player["location"]
        exitstr = ""
        exit_list = ["n", "s", "e", "w"]
        for exit in exit_list:
            if room[roomnum][exit]["leadsto"] != -1:
                if room[roomnum][exit]["isclosed"]:
                    exitstr += "<{}> ".format(exit)
                else:
                    exitstr += "{} ".format(exit)

        print("{}\n{}\n\nExits: {}\n".format(room[roomnum]['name'],
                                             room[roomnum]['desc'],
                                             exitstr))
        return room, player, False

    def open(room, player, args):
        roomnum = player["location"]
        # Handle invalid arguments
        if str(args[0]) in "nsew":
            dir_of_travel = str(args[0])
        else:
            print("Not a valid direction. Please use 'open [nsew]'.")
            return room, player, False
        if not room[roomnum][dir_of_travel]["isclosed"]:
            print("You can't open this door. The door is not closed.")
            return room, player, False
        elif room[roomnum][dir_of_travel]["islocked"]:
            print("You can't open this door. The door is locked.")
            return room, player, False
        elif room[roomnum][dir_of_travel]["isclosed"]:
            room[roomnum][dir_of_travel]["isclosed"] = False
            print("You open the door.")
            return room, player, False
        else:
            print("An unknown error has occurred. Please try again.")
            return room, player, False

    def close(room, player, args):
        roomnum = player["location"]
        # Handle invalid arguments
        if str(args[0]) in "nsew":
            dir_of_travel = str(args[0])
        else:
            print("Not a valid direction. Please use 'close [nsew]'.")
            return room, player, False
        if room[roomnum][dir_of_travel]["isclosed"]:
            print("You can't close this door. The door is already closed.")
            return room, player, False
        elif not room[roomnum][dir_of_travel]["isclosed"]:
            room[roomnum][dir_of_travel]["isclosed"] = True
            print("You close the door.")
            return room, player, False
        else:
            print("An unknown error has occurred. Please try again.")
            return room, player, False

    def unlock(room, player, args):
        roomnum = player["location"]
        # Handle invalid arguments
        if str(args[0]) in "nsew":
            dir_of_travel = str(args[0])
        else:
            print("Not a valid direction. Please use 'unlock [nsew]'.")
            return room, player, False
        if not room[roomnum][dir_of_travel]["isclosed"]:
            print("You can't unlock this door. The door is not closed.")
            return room, player, False
        elif not room[roomnum][dir_of_travel]["islocked"]:
            print("You can't unlock this door. The door is not locked.")
            return room, player, False
        elif room[roomnum][dir_of_travel]["islocked"]:
            room[roomnum][dir_of_travel]["islocked"] = False
            print("You unlock the door.")
            return room, player, False
        else:
            print("An unknown error has occurred. Please try again.")
            return room, player, False

    def exit(room, player, args):
        print("Thank you for playing. Goodbye!")
        return room, player, True

    # Main Library Logic Starts Here

    # Serves as a searchable index of commands and as a way to create command
    # aliases. Key is the command name or alias, and value is the function it
    # will invoke.
    index = {
        "look": look,
        "x": exit,
        "exit": exit,
        "open": open,
        "close": close,
        "unlock": unlock
        }

    # Invokes the defined function if the first item of the command list matches
    # a command listed in the index and then returns the return value of the
    # function. This allows each individual function to decide if the program
    # logic should continue or wait for further user input.
    if command[0] in index:
        return index[command[0]](room, player, command[1:])
    else:
        print("Command not found.")
        return room, player, False
