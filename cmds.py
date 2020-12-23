# All possible player commands must fall under the dispatcher function
# Returns True or False depending on if main loop should continue (True) or wait
# for additional player input (False).
def dispatcher(room, player, command):

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
        return False

    def exit(room, player, args):
        print("Thank you for playing. Goodbye!")
        return True

    index = { "look": look, "x": exit, "exit": exit }

    if command[0] in index:
        return index[command[0]](room, player, command[1:])
    else:
        print("Command not found.")
        return False
