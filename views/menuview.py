class MenuView():

    def __init__(self):
        pass

    def display_main_menu(self):
        """
        Prints the options available in the main menu.
        """
        print("Welcome to the main menu!")
        print("What would you like to do? Select the desired option by entering its number:")
        print("""
        1. Analyze file 1: data (20 actions)
        2. Quit the program
        """)
    
    def display_secondary_menu(self):
        """
        Prints the options available in the secondary menu.
        """
        print("\nWhat would you like to do? Select the desired option by entering its number:")
        print("""
        1. run the bruteforce algorithm
        2. run optimized algorithm
        3. Quit the secondary menu, and return main menu\n
        """)
  
    def error_choice_option(self):
        """Prints an error message when the user's input is not understood."""
        print("\nI did not understand your request, try again\n\n")