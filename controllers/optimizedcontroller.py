from utils.constant import Constant
from models.datamodel import DataModel

class OptimizedController():

    def __init__(self):
        self.constant = Constant()
        self.data_model = DataModel()

    def optimized(self, file_path):

        capital_to_invest = self.constant.constant_capital_invest()
        action_instances_list = self.data_model.creating_a_list_of_stock_market_instances(file_path)
        total_action = len(action_instances_list)

        matrix = [[0 for column  in range(3)] for row in range(total_action + 1)]
        # print(matrix)

        share_price = []
        profitability_of_an_share = []
        for share in action_instances_list:
            share_price.append(share.share_price)
            profitability_of_an_share.append(share.profitability_of_an_share)
        # print(share_price)
        # print(profitability_of_an_share)


