script_version = '0.0.1a'
keep_running = True
current_scroll = "PAPYRUS.txt"

def main():
    while keep_running == True:
        menu()
    else:
        print("Program exiting!")

def menu():
    print("[Insribing To: " + current_scroll + " ]")
    choice = str(input('Command: ')).capitalize() # Capitalize to make input
        # choices simpler.
    print("You typed: " + choice)
    if choice == "Q":
        global keep_running 
        keep_running = False # Quits program
    elif choice == "V":
        get_version()
    elif choice == "W":
        write_to_scroll()
    elif choice == "E":  
        # Confirm you actually want to erase the scroll
        confirm = str(input("This will erase a scroll -- ARE YOU SURE YOU WANT TO DO THIS? [Y/N] ")).capitalize()
        if confirm == "Y":
            erase_scroll()
        else:
            print("Aborting scroll erasure...")
    elif choice == "C":
        change_scroll()
    elif choice == "H":
        get_help()



def get_version():
    print(25 * '#')
    print("Script Version: " + script_version) 
    print(25 * '#')
    print("")

def write_to_scroll():
    message = input("Type inscription here: ")
    f = open(current_scroll, "a")
    f.write(message)
    f.close()
    print("Message inscribed!")

def erase_scroll():
    f = open(current_scroll, "w")
    f.write('')
    f.close()
    print("Scroll has been erased!")

def change_scroll():
    global current_scroll
    current_scroll = input("Enter file name: ")


def get_help():
    print("Available Commands:")
    commands = {
                "Q":"Quit the program.",
                "V":"Prints the program's version number.",
                "W":"Writes to the currently selected scroll.",
                "E":"Erases the current scroll. Must confirm 'Y' to proceed.",
                "C":"Changes the current scroll.",
                "H":"Prints this help menu."
               }
    for letter, description in commands.items():
        print("'" + letter + "'" + " = " + description)


# Start the program
print("For commands type 'H'")
main()

