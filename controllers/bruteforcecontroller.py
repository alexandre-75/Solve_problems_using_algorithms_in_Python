from models.bruteforcemodel import BruteForceModel


class BruteForceController():

    def __init__(self):
        self.brute_force_model = BruteForceModel()

    def brute_force(self, file_path):
        self.brute_force_model.creating_a_list_of_stock_market_instances(file_path)