from models.datamodel import DataModel

from views.bruteforceconstraintview import BruteForceConstraintView

from utils.constant import Constant


class BruteForceController():

    def __init__(self):
        self.data_model = DataModel()
        self.brute_force_constraint_view = BruteForceConstraintView()
        self.constant_capital_invest_util = Constant()

    def brute_force_constraint(self, file_path):

        dictionary = {}
        instances_list = self.data_model.creating_a_list_of_stock_market_instances(file_path)
        capital_to_invest = self.constant_capital_invest_util.constant_capital_invest()
        
        for instance in instances_list:

            name_of_an_stock_market = instance.name_of_an_action
            print(f"\non est dans l'action {name_of_an_stock_market}\n")
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
                    print(f"on est dans le if is_first_value and i.share_price <= capital_residual")
                    new_capital_invested = 0
                    number_of_stock_market_shares_2 = 0
                    while new_capital_invested <= capital_residual :
                        new_capital_invested += i.share_price
                        number_of_stock_market_shares_2 = number_of_stock_market_shares_2 + 1

                    capital_really_invested_2 =  new_capital_invested - i.share_price
                    number_of_stock_market_shares_2 = number_of_stock_market_shares_2 - 1
                    new_capital_residual = capital_residual - capital_really_invested_2
                    profits_2 = real_profit_of_an_action_after_two_years_2 *  number_of_stock_market_shares_2
                    for j in instances_list:
                        if j.share_price <= new_capital_residual:
                            print("         ------------ cas 6")
                            new_capital_invested_2 = 0
                            while new_capital_invested_2 <= new_capital_residual :
                                new_capital_invested_2 += j.share_price
                            capital_really_invested_3 =  new_capital_invested_2 - j.share_price
                            new_capital_residual_2 = new_capital_residual - capital_really_invested_3
                            for k in instances_list:
                                if k.share_price <= new_capital_residual_2:
                                    input()
                                else:
                                    pass
                        else:
                            pass

                    selected_instances[i.name_of_an_action] = [profits_2, number_of_stock_market_shares_2, capital_really_invested_2, new_capital_residual]
                    dictionnaire_trie_2 = dict(sorted(selected_instances.items(), key=lambda item: item[1], reverse=True))
                    second_key =list(dictionnaire_trie_2.keys())[0]
                    second_profit =list(dictionnaire_trie_2.values())[0][0]
                    second_number =list(dictionnaire_trie_2.values())[0][1]
                    second_capital =list(dictionnaire_trie_2.values())[0][2]

                elif i.share_price <= capital_residual:
                    print("  I am in case  2 ")
                    new_capital_invested = 0
                    while new_capital_invested <= capital_residual :
                        new_capital_invested += i.share_price
                    capital_really_invested_2 =  new_capital_invested - i.share_price
                    new_capital_residual = capital_residual - capital_really_invested_2
                    for j in instances_list:
                        if j.share_price <= new_capital_residual:
                            print("         ------------ cas 3")
                            new_capital_invested_2 = 0
                            while new_capital_invested_2 <= new_capital_residual :
                                new_capital_invested_2 += j.share_price
                            capital_really_invested_3 =  new_capital_invested_2 - j.share_price
                            new_capital_residual_2 = new_capital_residual - capital_really_invested_3
                            for k in instances_list:
                                if k.share_price <= new_capital_residual_2:
                                    print("             ------------------------ cas 4")
                                    new_capital_invested_3 = 0
                                    while new_capital_invested_3 <= new_capital_residual_2 :
                                        new_capital_invested_3 += k.share_price  
                                    capital_really_invested_4 =  new_capital_invested_3 - k.share_price
                                    new_capital_residual_3 = new_capital_residual_2 - capital_really_invested_4
                                    for h in instances_list:
                                        if h.share_price <= new_capital_residual_3:
                                            print("                         --------------------------- cas 5")
                                            new_capital_invested_4 = 0
                                            while new_capital_invested_4 <= new_capital_residual_3 :
                                                new_capital_invested_4 += h.share_price                                           
                                            capital_really_invested_5 =  new_capital_invested_4 - h.share_price
                                            new_capital_residual_4 = new_capital_residual_3 - capital_really_invested_5
                                            for m in instances_list:
                                                if m.share_price <= new_capital_residual_4:
                                                    input()
                                                else:
                                                    pass
                                        else:
                                            pass
                                else:
                                    pass
                        else:
                            pass
                else:
                    pass

        self.brute_force_constraint_view.display_best_investment(dictionnaire_trie)
        self.brute_force_constraint_view.display_best_investment(dictionnaire_trie_2)
        self.brute_force_constraint_view.display_resume_best_investment(first_key, second_key, first_number, second_number, first_profit, second_profit)

