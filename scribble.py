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

def get_version():
    print(15 * '#')
    print("Script Version: " + script_version) 
    print(15 * '#')
    print("")

# Start the program
main()

