from models.bruteforcemodel import BruteForceModel

from utils.time import Time
from utils.constant import Constant


class BruteForceController():

    def __init__(self):
        self.brute_force_model = BruteForceModel()
        self.time_util = Time()
        self.constant_capital_invest_util = Constant()

    def brute_force(self, file_path):
        instances_list = self.brute_force_model.creating_a_list_of_stock_market_instances(file_path)
        time_start = self.time_util.time()
        capital_to_invest = self.constant_capital_invest_util.constant_capital_invest()
        for instance in instances_list:

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


            print(f"capital investi : {capital_really_invested}")
            print(f"action :{number_of_stock_market_shares}")
            print(f"profits :{profits}")
            print(capital_residual)
