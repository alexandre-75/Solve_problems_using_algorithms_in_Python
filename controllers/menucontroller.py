from views.menuview import MenuView


class MenuController():

    def __init__(self):
        self.menu_view = MenuView()

    def main_menu(self):
        self.menu_view.display_main_menu()
        user_input = input("enter a value, please : ")
        if user_input == "1":
            pass
        elif user_input == "2":
            return exit()
        else:
            self.menu_view.error_choice_option()
            return self.main_menu()