from views.menuview import MenuView


class MenuController():

    def __init__(self):
        self.menu_view = MenuView()

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
            pass
        elif user_input == "2":
            pass
        elif user_input =="3":
            return self.main_menu()
        else:
            self.menu_view.error_choice_option()
            return self.secondary_menu_choice_of_program()
        