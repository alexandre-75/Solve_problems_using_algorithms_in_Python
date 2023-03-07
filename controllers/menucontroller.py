from views.menuview import MenuView
from controllers.bruteforcecontroller import BruteForceController


class MenuController():

    def __init__(self):
        self.menu_view = MenuView()
        self.brute_force_controller = BruteForceController()

    def main_menu(self):
        self.menu_view.display_main_menu()
        user_input = input("enter a value, please : ")
        if user_input == "1":
            return self.secondary_menu_choice_of_program()     
        elif user_input == "2":
            return exit()
        else:
            self.menu_view.error_choice_option()
            return self.main_menu()
    
    def secondary_menu_choice_of_program (self):
        self.menu_view.display_secondary_menu()
        user_input = input("enter a value, please : ")
        if user_input == "1":
            file_path = "data\data.csv"
            self.brute_force_controller.brute_force(file_path)
        elif user_input == "2":
            pass
        elif user_input =="3":
            return self.main_menu()
        else:
            self.menu_view.error_choice_option()
            return self.secondary_menu_choice_of_program()
        