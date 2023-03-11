from itertools import combinations

from views.bruteforceview import BruteForceView
from models.datamodel import DataModel
from utils.constant import Constant


class BruteForceController ():

    def __init__(self):

        self.brute_force_view = BruteForceView()
        self.data_model = DataModel()
        self.constant_capital_invest_util = Constant()
    
    def brute_force(self, file_path):

        u = 0
        list_best_investment = []
        for i in range(20):
            u = i + 1
            capital_to_invest = self.constant_capital_invest_util.constant_capital_invest()

            action_instances_list = self.data_model.creating_a_list_of_stock_market_instances(file_path)
            all_combinations = list(combinations(action_instances_list, u))

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

        if list_best_investment:
            list_best_investment.sort(key=lambda x: sum([(e.share_price/100) * e.profitability_of_an_share for e in x]), reverse=True)
            best_of_the_best = list_best_investment[0]
            
        self.brute_force_view.display_best_of_the_best(best_of_the_best)
