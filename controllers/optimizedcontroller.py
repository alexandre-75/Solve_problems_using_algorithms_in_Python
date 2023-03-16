from utils.constant import Constant
from models.datamodel import DataModel
from controllers.stockcontroller import Stock

class OptimizedController():

    def __init__(self):
        self.constant = Constant()
        self.data_model = DataModel()

    def optimized(self, file_path):

        capital_to_invest = self.constant.constant_capital_invest()
        action_instances_list = self.data_model.creating_a_list_of_stock_market_instances(file_path)
        total_action = len(action_instances_list)

        matrix = [[0 for column  in range(capital_to_invest + 1)] for row in range(total_action + 1)]

        share_price = []
        profitability_of_an_share = []
        list_profit = []
        for share in action_instances_list:
            share_price.append(share.share_price)
            profitability_of_an_share.append(share.profitability_of_an_share)
            list_profit.append((share.share_price/100)*share.profitability_of_an_share)
      
        for nb_of_share in range(1, total_action + 1):
            current_share = action_instances_list[nb_of_share-1]
            for evolving_capital in range (1, capital_to_invest + 1):
                if current_share.share_price <= evolving_capital:
                    matrix[nb_of_share][evolving_capital] = max(matrix[nb_of_share-1][evolving_capital], list_profit[nb_of_share-1] + matrix[nb_of_share-1][evolving_capital-share_price[nb_of_share-1]])
                else:
                    matrix[nb_of_share][evolving_capital] = matrix[nb_of_share-1][evolving_capital]

        stock_selection = []
        while capital_to_invest >= 0 and total_action >=0:
            stock = action_instances_list[total_action - 1]
            if matrix[int(total_action)][int(capital_to_invest)] == matrix[int(total_action)-1][int(capital_to_invest - stock.share_price)] + stock.profit2:
                stock_selection.append(stock)
                capital_to_invest -= stock.share_price
            total_action -= 1
        return matrix[-1][-1], stock_selection
