class MenuView():

    def __init__(self):
        pass

    def display_main_menu(self):
        """
        Prints the options available in the main menu.
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nWelcome to the main menu!")
        print("What would you like to do? Select the desired option by entering its number:")
        print("""
        1. Analyze file 1: data (20 actions)
        2. Quit the program
        """)

    def display_secondary_menu(self):
        """
        Prints the options available in the secondary menu.
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nWelcome to the secondary menu!")
        print("What would you like to do? Select the desired option by entering its number:")
        print("""
        1. Quit the secondary menu, and return main menu
        2. Menu : Run brute force program
        3. Run optimized program
        """)

    def display_program_choice_third_menu(self):
        """
        Prints the options available in the thrid menu.
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nWelcome to the thrid menu!")
        print("What would you like to do? Select the desired option by entering its number:")
        print("""
        1. Quit the trid menu, and return secondary menu\n
        2. Quit the trid menu, and return main menu\n
        3. Run brute force :
            constraint : the same share is purchased as long as the capital is available. Then we start again with the remaining capital.\n
        4. Run brute force :
            constraint: Each share can only be purchased once.
        """)

    def error_choice_option(self):
        """Prints an error message when the user's input is not understood."""
        print("\nI did not understand your request, try again\n\n")