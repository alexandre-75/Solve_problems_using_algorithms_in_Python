from time import perf_counter
from itertools import combinations

from views.bruteforceview import BruteForceView
from models.datamodel import DataModel
from utils.constant import Constant

import matplotlib.pyplot as plt
import math


class BruteForceController ():

    def __init__(self):

        self.brute_force_view = BruteForceView()
        self.data_model = DataModel()
        self.constant_capital_invest_util = Constant()
    
    def brute_force(self, file_path):

        start_time = perf_counter() # start program execution time
        execution_times = []
        num_actions_available = []
        u = 0
        list_best_investment = []

        start_time = perf_counter()
        for i in range(20):
            u = i + 1
            capital_to_invest = self.constant_capital_invest_util.constant_capital_invest()

            action_instances_list = self.data_model.creating_a_list_of_stock_market_instances(file_path)
            all_combinations = list(combinations(action_instances_list, u))

            start_time_boucle = perf_counter() # starts to calculate the execution time of a combination
            combinations_below_budget_max = []
            for combination in all_combinations:

                list_sum_price = []
                for element in combination:
                    list_sum_price.append(element.share_price)
                total_list_sum_price = sum(list_sum_price)
                if total_list_sum_price <= capital_to_invest:
                    combinations_below_budget_max.append(combination)
                else:
                    pass
            if combinations_below_budget_max:
                combinations_below_budget_max.sort(key=lambda x: sum([(e.share_price/100) * e.profitability_of_an_share for e in x]), reverse=True)
                best_investment = combinations_below_budget_max[0]
                list_best_investment.append(best_investment)
            
            end_time_boucle = perf_counter() # finished calculating the execution time of a combination
            execution_time_boucle = end_time_boucle - start_time_boucle
            execution_times.append(execution_time_boucle)
            num_actions_available.append(u)

        if list_best_investment:
            list_best_investment.sort(key=lambda x: sum([(e.share_price/100) * e.profitability_of_an_share for e in x]), reverse=True)
            best_of_the_best = list_best_investment[0]
            
        self.brute_force_view.display_best_of_the_best(best_of_the_best)

        end_time = perf_counter() # end program execution time
        execution_time = end_time - start_time

        self.brute_force_view.display_execution_time(execution_time)

        user_input = int(input("\ntype [1] to see the graphics that summarize the program otherwise type [2] : "))

        if user_input == 1:

            # Plot the execution time against the number of actions available
            plt.subplot(1, 2, 1)
            plt.plot(num_actions_available, execution_times, 'r+', markersize=5) 
            x = range(1, 21)
            y = [math.factorial(i) for i in x]
            plt.xlabel('actions')
            plt.ylabel('Execution time (seconds)')
            plt.title('Execution time of Brute Force method')
            
            plt.subplot(1, 2, 2)
            num_branches = [len(list(combinations(self.data_model.creating_a_list_of_stock_market_instances(file_path), i))) for i in range(1, 21)]
            plt.plot(num_actions_available, num_branches, 'b+', markersize=5)
            plt.xlabel('actions')
            plt.ylabel('Number of branches')
            plt.title('Number of branches of Brute Force method')

            plt.show()
        else:
            pass