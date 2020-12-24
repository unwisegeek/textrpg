import art, json, os, subprocess, string, random
from time import sleep
from rooms import room_template, room_num_exists

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
room = []
proceed = False
loaded_map = ""

def cls():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

# Start main Logic
cls()
print ("Welcome to...")
art.tprint("Map Editor", font="tinker-toy")
print("\n\n")

while choice not in EXIT_COMMANDS and not proceed:
    choice = input("Do you wish to start a [new] map, [load] a saved map, "
                    "or [list] saved maps? ")

    if choice == "new":
        room = [ room_template ]
        proceed = True
        continue

    if choice == "list":
        for file in os.listdir(os.getcwd()):
            if file.endswith(".map"):
                print(file)
        continue

    if choice == "load":
        filename = input("Please enter the filename you wish to load, "
                         "with or without the .map exension: ")
        try:
            if filename.endswith(".map"):
                file = open(filename, 'r')
            else:
                file = open("{}.map".format(filename), 'r')
                filename += ".map"
        except:
            print("Could not open file for reading.")
            sleep(1)
        else:
            room = json.loads(file.read())
            loaded_map = filename
            proceed = True
            continue

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
        leadsto = room[index][dir]["leadsto"]
        if leadsto == -1:
            leadsto_name = "No Exit"
        else:
            leadsto_name = room[leadsto]["name"]
        isclosed = str(room[index][dir]["isclosed"])
        islocked = str(room[index][dir]["islocked"])

        print("{:>6} {}. Leads to: {:>6} [{:>30}] | {}. Closed: {:>5} | {}. Locked: {:>5}".format(
        dir_name, opt1, leadsto, leadsto_name, opt2, isclosed, opt3, islocked))
        option_index[opt1] = [dir, "leadsto"]
        option_index[opt2] = [dir, "isclosed"]
        option_index[opt3] = [dir, "islocked"]
        opt_list_index += 3
    print("\n\n")
    choice = input("Please enter your selection: ")

    # Bypass this logic if a quit command is received.
    if choice in EXIT_COMMANDS:
        continue

    if choice == ">":
        try:
            t=room[index+1]["name"]
        except IndexError:
            index = 0
            continue
        else:
            index += 1
            continue

    if choice == "<":
        if index > 0:
            try:
                t=room[index-1]["name"]
            except IndexError:
                index = len(room) - 1
                continue
            else:
                index -= 1
        else:
            index = len(room) - 1
            continue

    if choice == "save":
        if loaded_map == "":
            filename = input("Please enter the filename, "
                            "with or without .map extension: ")
        else:
            filename = input("Please enter the filename, with or without"
                             ".map extension: [{}] ".format(loaded_map))
            if filename == "":
                filename = loaded_map
        try:
            if filename.endswith(".map"):
                file = open(filename, 'w')
            else:
                file = open("{}.map".format(filename), 'w')
        except:
            print("Could not open file for writing.")
            continue
        else:
            file.write(json.dumps(room))
            file.close()
            print("File written.")
            continue
        continue

    if choice in option_index:
        proceed = False
        # Room Number
        if option_index[choice][1] == "num":
            while not proceed:
                user_input = input("Please enter a room number: ")
                # Validate input. Must be 0-99999 and not be assigned to another
                # room.
                try:
                    t = int(user_input)
                except ValueError:
                    print("Room number must be a number!")
                    sleep(1)
                    continue
                else:
                    new_number = int(user_input)
                    if 0 < new_number < 99999:
                        if not room_num_exists(room, new_number) or \
                        new_number == room[index]["num"]:
                            # Tests pass.
                            room[index]["num"] = new_number
                            proceed = True
                        else:
                            print("Number already exists!")
                            continue
                    else:
                        print("The number must be higher than 0 and lower than 99999.")
                        continue

        if option_index[choice][1] == "name":
            user_input = ""
            proceed = False
            while not proceed:
                user_input = input("Please enter a room name: ")
                # Validate input. Must be a string and not blank.
                if user_input == "":
                    print("Cannot accept a blank string.")
                else:
                    room[index]["name"] = user_input
                    proceed = True

        if option_index[choice][1] == "desc":
            # Get a temporary file name
            random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])
            tmp_filename = "{}.tmp".format(random_string)
            # If a description for the room isn't blank, load it into the
            # temporary file.
            if room[index]["desc"] != "":
                file = open(tmp_filename, 'w')
                file.write(room[index]["desc"])
                file.close()
            # Open the file in editor. Change this later.
            if os.name == "nt":
                p = subprocess.Popen("notepad {}".format(tmp_filename), shell=True)
                # Wait for notepad to close before continuing program execution
                process_state = p.poll()
                while process_state == None:
                    process_state = p.poll()
            else:
                p = subprocess.Popen("editor {}".format(tmp_filename), shell=True)

            # Read the contents of the temp file and assign it to the room db
            file = open(tmp_filename, 'r')
            contents = file.read()
            file.close()
            try:
                os.remove(tmp_filename)
            except:
                input("Can't delete temporary files. Please remove all .tmp "
                      "files from the script directory at your earliest"
                      "convenience. Press enter to continue.")
            # Write the new desc to the room db
            room[index]["desc"] = contents
            continue

    # Handle true/false toggle values.
    if option_index[choice][1] in ["leadsto", "isclosed", "islocked"]:
        dir = option_index[choice][0]
        value = option_index[choice][1]
        if room[index][dir][value]:
            room[index][dir][value] = False
            continue
        else:
            room[index][dir][value] = True
            continue
        continue

    if choice == "pio":
        print(option_index)
        input("Press enter to continue.")
