from time import perf_counter

from utils.constant import Constant
from models.datamodel import DataModel
from controllers.stockcontroller import Stock
from views.optimizedview import OptimizedView

class OptimizedController():

    def __init__(self):
        self.constant = Constant()
        self.data_model = DataModel()
        self.optimized_view = OptimizedView()

    def optimized(self, file_path):

        """Optimizes an investment portfolio using the knapsack optimization algorithm.

         The knapsack optimization algorithm is a classic algorithm in computer science 
         that solves a combinatorial optimization problem,
         which consists of filling a bag with objects of different sizes and values 
         while maximizing the total value of the objects in the bag and respecting the maximum capacity of the bag.
         In this case, stock market shares are the objects and the capital available to invest is the maximum capacity of the bag.

         args:
             file_path (str): The path to the file containing the stock market stock information.

         Returns:
             None

         """

        start_time = perf_counter()

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
        
        end_time = perf_counter()
        total_time = end_time - start_time

        self.optimized_view.display_resume_investment(matrix[-1][-1], stock_selection, total_time)

