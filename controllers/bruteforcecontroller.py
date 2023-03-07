from models.bruteforcemodel import BruteForceModel

from views.bruteforceview import BruteForceView

from utils.time import Time
from utils.constant import Constant


class BruteForceController():

    def __init__(self):
        self.brute_force_model = BruteForceModel()
        self.brute_force_view = BruteForceView()
        self.time_util = Time()
        self.constant_capital_invest_util = Constant()

    def brute_force(self, file_path):
        instances_list = self.brute_force_model.creating_a_list_of_stock_market_instances(file_path)
        time_start = self.time_util.time()
        capital_to_invest = self.constant_capital_invest_util.constant_capital_invest()
        dictionary= {}
        list_name_action = []
        list_number_of_stock_market_shares = []
        list_global_profits_after_two_years= []


        for instance in instances_list:

            name_of_an_stock_market = instance.name_of_an_action
            price_of_a_stock_market = instance.share_price
            percentage_profit_after_two_years = instance.profitability_of_an_share

            real_profit_of_an_action_after_two_years = float((price_of_a_stock_market / 100) * percentage_profit_after_two_years)

            invested_capital = 0
            number_of_stock_market_shares = 0
            while invested_capital <= capital_to_invest :
                invested_capital += instance.share_price
                number_of_stock_market_shares =  number_of_stock_market_shares + 1

            capital_really_invested = invested_capital - price_of_a_stock_market
            number_of_stock_market_shares =  number_of_stock_market_shares - 1
            capital_residual = capital_to_invest - capital_really_invested
            profits = real_profit_of_an_action_after_two_years * number_of_stock_market_shares

            dictionary[name_of_an_stock_market] = [profits, number_of_stock_market_shares, capital_residual]
            list_name_action.append(name_of_an_stock_market)
            list_number_of_stock_market_shares.append(number_of_stock_market_shares)
            list_global_profits_after_two_years.append(profits)

            # print(f"capital investi : {capital_really_invested}")
            # print(f"action :{number_of_stock_market_shares}")
            # print(f"profits :{profits}")
            # print(capital_residual)
        # print(dictionary)
            # print(len(dictionary))

        dictionnaire_trie = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

        self.brute_force_view.display_profits(list_name_action, list_number_of_stock_market_shares, list_global_profits_after_two_years)
        self.brute_force_view.display(dictionnaire_trie)

        # print(list_name_action)
        # print(dictionnaire_trie["Action-10"])
        # print(dictionnaire_trie)


        # print(list_name_action)
        # print(len(list_name_action))
        # print(list_global_profits_after_two_years)
        # print(len(list_global_profits_after_two_years))
        # print(list_number_of_stock_market_shares)
        # print(len(list_number_of_stock_market_shares))

        
