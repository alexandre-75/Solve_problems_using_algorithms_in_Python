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

        dictionary= {}
        list_name_action = []
        list_number_of_stock_market_shares = []
        list_global_profits_after_two_years= []

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

            dictionary[name_of_an_stock_market] = [profits, number_of_stock_market_shares, capital_residual]
            list_name_action.append(name_of_an_stock_market)
            list_number_of_stock_market_shares.append(number_of_stock_market_shares)
            list_global_profits_after_two_years.append(profits)

            print("\n\n")
            print(f"capital investi : {capital_really_invested}")
            print(f"action :{number_of_stock_market_shares}")
            print(f"profits :{profits}")
            print(f"capital_residual: {capital_residual}")

            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for i in instances_list:

                percentage_profit_after_two_years_2 = i.profitability_of_an_share
                real_profit_of_an_action_after_two_years_2 = float((i.share_price / 100) * percentage_profit_after_two_years_2)

                if i.share_price <= capital_residual :
                    print(f"je peux encore acheter cette actions {i.name_of_an_action}")
                    print(f"prix d'une action {i.share_price}")
                    new_capital_invested = 0
                    number_of_stock_market_shares_2 = 0
                    while new_capital_invested <= capital_residual :
                        new_capital_invested += i.share_price
                        number_of_stock_market_shares_2 = number_of_stock_market_shares_2 + 1

                    capital_really_invested_2 =  new_capital_invested - i.share_price
                    number_of_stock_market_shares_2 = number_of_stock_market_shares_2 - 1
                    new_capital_residual = capital_residual - capital_really_invested_2
                    profits_2 = real_profit_of_an_action_after_two_years_2 *  number_of_stock_market_shares_2

                    print(f"nouveau capital à investir:  {capital_residual}")
                    print(f"capital réélement investi: {capital_really_invested_2}")
                    print( f"nombre actions: {number_of_stock_market_shares_2}")
                    print(f"capital restant a investir:  {new_capital_residual}")
                    print(f"profits_2: {profits_2}")

                    for j in instances_list:

                        percentage_profit_after_two_years_3 = j.profitability_of_an_share
                        real_profit_of_an_action_after_two_years_3 = float((j.share_price / 100) * percentage_profit_after_two_years_3)

                        if j.share_price <= new_capital_residual:
                            print(f"heureka j'investi encore {j.share_price}")
                            print(f"prix d'une action {j.share_price}")
                            new_capital_invested_2 = 0
                            number_of_stock_market_shares_3 = 0
                            while new_capital_invested_2 <= new_capital_residual :
                                new_capital_invested_2 += j.share_price
                                number_of_stock_market_shares_3 = number_of_stock_market_shares_3 + 1
                            
                            capital_really_invested_3 =  new_capital_invested_2 - j.share_price
                            number_of_stock_market_shares_3 = number_of_stock_market_shares_3 - 1
                            new_capital_residual_2 = new_capital_residual - capital_really_invested_3
                            profits_3 = real_profit_of_an_action_after_two_years_3 *  number_of_stock_market_shares_3
                        
                            print(f"nouveau capital à investir:  {new_capital_residual}")
                            print(f"capital réélement investi: {capital_really_invested_3}")
                            print( f"nombre actions: {number_of_stock_market_shares_3}")
                            print(f"capital restant a investir:  {new_capital_residual_2}")
                            print(f"profits_2: {profits_3}")
                            print("-------------------------------------------------------")

                            for k in instances_list:

                                percentage_profit_after_two_years_4 = k.profitability_of_an_share
                                real_profit_of_an_action_after_two_years_4 = float((k.share_price / 100) * percentage_profit_after_two_years_4)

                                if k.share_price <= new_capital_residual_2:
                                    print(f"je cherche la fin  {k.share_price}")
                                    print(f"prix d'une action {k.share_price}")
                                    new_capital_invested_3 = 0
                                    number_of_stock_market_shares_4 = 0
                                    while new_capital_invested_3 <= new_capital_residual_2 :
                                        new_capital_invested_3 += k.share_price
                                        number_of_stock_market_shares_4 = number_of_stock_market_shares_4 + 1
                                    
                                    capital_really_invested_4 =  new_capital_invested_3 - k.share_price
                                    number_of_stock_market_shares_4 = number_of_stock_market_shares_4 - 1
                                    new_capital_residual_3 = new_capital_residual_2 - capital_really_invested_4
                                    profits_4 = real_profit_of_an_action_after_two_years_4 *  number_of_stock_market_shares_4
                                
                                    print(f"nouveau capital à investir:  {new_capital_residual_2}")
                                    print(f"capital réélement investi: {capital_really_invested_4}")
                                    print( f"nombre actions: {number_of_stock_market_shares_4}")
                                    print(f"capital restant a investir:  {new_capital_residual_3}")
                                    print(f"profits_2: {profits_4}")
                                    print("-------------------------------------------------------")

                                    for h in instances_list:
                                        percentage_profit_after_two_years_5 = h.profitability_of_an_share
                                        real_profit_of_an_action_after_two_years_5 = float((h.share_price / 100) * percentage_profit_after_two_years_5)

                                        if h.share_price <= new_capital_residual_3:
                                            print(input())
                                            print(f"je cherche la fin  {h.share_price}")
                                            print(f"prix d'une action {h.share_price}")
                                            new_capital_invested_4 = 0
                                            number_of_stock_market_shares_5 = 0
                                            while new_capital_invested_4 <= new_capital_residual_3 :
                                                new_capital_invested_4 += h.share_price
                                                number_of_stock_market_shares_5 = number_of_stock_market_shares_5 + 1
                                            
                                            capital_really_invested_5 =  new_capital_invested_4 - h.share_price
                                            number_of_stock_market_shares_5 = number_of_stock_market_shares_5 - 1
                                            new_capital_residual_4 = new_capital_residual_3 - capital_really_invested_5
                                            profits_5 = real_profit_of_an_action_after_two_years_5 *  number_of_stock_market_shares_5
                                        
                                            print(f"nouveau capital à investir:  {new_capital_residual_3}")
                                            print(f"capital réélement investi: {capital_really_invested_5}")
                                            print( f"nombre actions: {number_of_stock_market_shares_5}")
                                            print(f"capital restant a investir:  {new_capital_residual_4}")
                                            print(f"profits_2: {profits_5}")
                                            print("-------------------------------------------------------")
                                        else:
                                            # print("n")
                                            pass         
                                else:
                                    # print("enfin")
                                    pass
                        else:
                            # print("la fete est fini")
                            pass
                else:
                    # print(f"je peux plus ivestir dans {i.name_of_an_action}")
                    pass
                
        # print(dictionary)
            # print(len(dictionary))
        dictionnaire_trie = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

        # self.brute_force_view.display_profits(list_name_action, list_number_of_stock_market_shares, list_global_profits_after_two_years)
        # self.brute_force_view.display(dictionnaire_trie)

        # print(list_name_action)
        # print(dictionnaire_trie["Action-10"])
        # print(dictionnaire_trie)


        # print(list_name_action)
        # print(len(list_name_action))
        # print(list_global_profits_after_two_years)
        # print(len(list_global_profits_after_two_years))
        # print(list_number_of_stock_market_shares)
        # print(len(list_number_of_stock_market_shares))

        
