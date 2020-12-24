import art, json, os
from time import sleep

# Initial Variables
index = 0
choice = ""
dir_list_index = 0
opt_list_index = 0
EXIT_COMMANDS = ["quit", "exit", "ex"]
DIR_LIST = [["North:", "n"], ["South:", "s"], ["East:", "e"], ["West:", "w"]]
OPT_LIST = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"]
option_index = {}

# Load default map file
file = open('roomfile', 'r')
room = json.loads(file.read())

def cls():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

while choice not in EXIT_COMMANDS:
    cls()
    option_index = {}
    art.tprint("Map Editor", font="tinker-toy")
    print("Index: {:>4}".format(index))
    print("a. Room Number: {:>4}".format(room[index]["num"]))
    print("b. Room Name: {}".format(room[index]["name"]))
    print("c. Room Description: {}\n\n".format(room[index]["desc"]))
    opt_list_index = 3 # Set to the following index number.
    option_index["a"] = [False, "num"]
    option_index["b"] = [False, "name"]
    option_index["c"] = [False, "desc"]



    # Generate the editor layout for directional entries.
    for i in range(0, len(DIR_LIST)):
        dir_name, dir = DIR_LIST[i][0], DIR_LIST[i][1]
        opt1, opt2, opt3 = OPT_LIST[opt_list_index], \
                           OPT_LIST[opt_list_index + 1], \
                           OPT_LIST[opt_list_index + 2]

        print("{:>6} {}. Leads to: {:>4} | {}. Closed: {:>5} | {}. Locked: {:>5}".format(
        dir_name, opt1, room[index][dir]["leadsto"], opt2, str(room[index][dir]["isclosed"]),
        opt3, str(room[index][dir]["islocked"])
        ))
        option_index[opt1] = [dir, "leadsto"]
        option_index[opt2] = [dir, "isclosed"]
        option_index[opt3] = [dir, "islocked"]
        opt_list_index += 3
    print("\n\n")
    choice = input("Please enter your selection: ")

    if choice == ">":
        try:
            t=room[index+1]["name"]
        except IndexError:
            index = 0
        else:
            index += 1

    if choice == "<":
        if index > 0:
            try:
                t=room[index-1]["name"]
            except IndexError:
                index = len(room)
            else:
                index -= 1
        else:
            index = len(room) - 1
