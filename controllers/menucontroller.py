from views.menuview import MenuView


class MenuController():
    def __init__(self):
        self.menu_view = MenuView()
    
    def main_menu(self):
        # while True:
        self.menu_view.display_main_menu()
        print("end")