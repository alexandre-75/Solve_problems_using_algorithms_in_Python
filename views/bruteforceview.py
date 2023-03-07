from prettytable import PrettyTable


class BruteForceView():

    def __init__(self):
        self.table = PrettyTable()
        self.display_report_header_brute_force = ["actions", "number_of_stock_market_shares", "global_profits_after_two_years"]
    
    def display_profits(self, list_actions, list_stock_market_shares, list_global_profits):
        self.table = PrettyTable()
        self.table.field_names = self.display_report_header_brute_force
        for i in range(len(list_actions)):
            self.table.add_row([list_actions[i], list_stock_market_shares[i], list_global_profits[i]])
        print(self.table)

    def display(self, dictionnaire_trie):
        for key, values in dictionnaire_trie.items():
            print("\n----------------------------")
            print(f"{key}:")
            print(f"profit: {values[0]}")
            print(f"number of stock market shares: {values[1]}")
            print(f"capital residual: {values[2]}")

