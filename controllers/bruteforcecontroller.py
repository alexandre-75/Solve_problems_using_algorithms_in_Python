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

        dictionary = {}
        instances_list = self.brute_force_model.creating_a_list_of_stock_market_instances(file_path)
        time_start = self.time_util.time()
        capital_to_invest = self.constant_capital_invest_util.constant_capital_invest()
        
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

            dictionary[name_of_an_stock_market] = [profits, number_of_stock_market_shares, capital_really_invested, capital_residual]
            dictionnaire_trie = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
            first_key = list(dictionnaire_trie.keys())[0]
            first_profit = list(dictionnaire_trie.values())[0][0]
            first_number = list(dictionnaire_trie.values())[0][1]
            first_capital = list(dictionnaire_trie.values())[0][2]

            is_first_value = name_of_an_stock_market == first_key
            selected_instances = {}

            for i in instances_list:
               
                percentage_profit_after_two_years_2 = i.profitability_of_an_share
                real_profit_of_an_action_after_two_years_2 = float((i.share_price / 100) * percentage_profit_after_two_years_2)

                if is_first_value and i.share_price <= capital_residual:
                    new_capital_invested = 0
                    number_of_stock_market_shares_2 = 0
                    while new_capital_invested <= capital_residual :
                        new_capital_invested += i.share_price
                        number_of_stock_market_shares_2 = number_of_stock_market_shares_2 + 1

                    capital_really_invested_2 =  new_capital_invested - i.share_price
                    number_of_stock_market_shares_2 = number_of_stock_market_shares_2 - 1
                    new_capital_residual = capital_residual - capital_really_invested_2
                    profits_2 = real_profit_of_an_action_after_two_years_2 *  number_of_stock_market_shares_2

                    selected_instances[i.name_of_an_action] = [profits_2, number_of_stock_market_shares_2, capital_really_invested_2, new_capital_residual]
                    dictionnaire_trie_2 = dict(sorted(selected_instances.items(), key=lambda item: item[1], reverse=True))
                    second_key =list(dictionnaire_trie_2.keys())[0]
                    second_profit =list(dictionnaire_trie_2.values())[0][0]
                    second_number =list(dictionnaire_trie_2.values())[0][1]
                    second_capital =list(dictionnaire_trie_2.values())[0][2]
                else:
                    pass

        self.brute_force_view.display_best_investment(dictionnaire_trie)
        self.brute_force_view.display_best_investment(dictionnaire_trie_2)
        self.brute_force_view.display_resume_best_investment(first_key, second_key, first_number, second_number, first_profit, second_profit)

        end_time = self.time_util.time()
        program_execution_time = end_time - time_start
        self.brute_force_view.display_program_execution_time(program_execution_time)
        user_input = input("\ntype [a] to exit : ")
        if user_input == "a":
            return exit()
            