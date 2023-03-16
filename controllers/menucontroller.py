from views.menuview import MenuView
from views.bruteforceconstraintview import BruteForceConstraintView

from controllers.bruteforceconstraintcontroller import BruteForceConstraintController
from controllers.bruteforcecontroller import BruteForceController
from controllers.optimizedcontroller import OptimizedController

from time import perf_counter


class MenuController():

    def __init__(self):

        self.menu_view = MenuView()
        self.brute_force_constraint_view = BruteForceConstraintView()

        self.brute_force_constraint_controller = BruteForceConstraintController()
        self.brute_force_controller = BruteForceController()
        self.optimized_controller = OptimizedController()

    def main_menu(self):
        self.menu_view.display_main_menu()
        file_path_2 = "data\dataset1_Python+P7.csv"
        file_path_3 = "data\dataset2_Python+P7.csv"
        user_input = input("enter a value, please : ")
        if user_input == "1":
            return self.secondary_menu_choice_of_program() 
        elif  user_input == "2":
            return self.management_file(file_path_2)
        elif  user_input == "3":
            return self.management_file(file_path_3)
        elif user_input == "4":
            return exit()
        else:
            self.menu_view.error_choice_option()
            return self.main_menu()
    
    def secondary_menu_choice_of_program (self):
        file_path = "data\data.csv"
        file_path_2 = "data\dataset1_Python+P7.csv"
        self.menu_view.display_secondary_menu()
        user_input = input("enter a value, please : ")
        if user_input == "1":
            return self.main_menu()
        elif user_input =="2":
            return self.program_choice_third_menu(file_path)
        elif user_input =="3":
            return self.management_optimized(file_path)
        else:
            self.menu_view.error_choice_option()
            return self.secondary_menu_choice_of_program()
        
    def program_choice_third_menu(self, file_path):
        self.menu_view.display_program_choice_third_menu()
        user_input = input("enter a value, please : ")
        if user_input =="1":
            return self.secondary_menu_choice_of_program()
        if user_input =="2":
            return self.main_menu()
        if user_input =="3":
            return self.management_brute_force_constraint(file_path)
        if user_input =="4":
            return self.management_brute_force(file_path)
        else:
            self.menu_view.error_choice_option()
            return self.program_choice_third_menu()
        
    def management_brute_force_constraint(self, file_path):
        start_timer = perf_counter()
        self.brute_force_constraint_controller.brute_force_constraint(file_path)
        end_timer = perf_counter()
        bruteforce_time = end_timer - start_timer
        self.brute_force_constraint_view.display_program_execution_time(bruteforce_time)
        user_input = int(input("\npress [1] to return to the third menu, otherwise main menu : "))
        if user_input == 1:
            return self.program_choice_third_menu(file_path)
        else:
            return self.main_menu()

    def management_brute_force(self, file_path):
        self.brute_force_controller.brute_force(file_path)
        user_input = int(input("\npress [1] to exit the program: "))
        if user_input == 1:
            return self.program_choice_third_menu(file_path)
        else:
            return self.main_menu()
    
    def management_optimized(self, file_path):
        self.optimized_controller.optimized(file_path)
        user_input = int(input("\npress [1] to exit the program: "))
        if user_input == 1:
            return self.secondary_menu_choice_of_program()
        else:
            return self.main_menu()
    
    def management_file(self, file_path):
        self.optimized_controller.optimized(file_path)
        user_input = int(input("\npress [1] to exit the program: "))
        if user_input == 1:
            return self.main_menu()
        else:
            pass
        
