script_version = '0.0.1a'
keep_running = True

def main():
    while keep_running == True:
        menu()
    else:
        print("Program exiting!")

def menu():
    choice = str(input('Command: ')).capitalize() # Capitalize to make input
        # choices simpler.
    print("You typed: " + choice)


# Start the program
main()

