from controllers.stockcontroller import Stock
import csv

class DataModel():

    def __init__(self):
        pass

    def creating_a_list_of_stock_market_instances(self, file_path):

        """
        Reads a CSV file containing stock market data and returns a list of `Stock` instances.

        Args:
            file_path: A string containing the path to the CSV file.

        Returns:
            A list of `Stock` instances, where each instance corresponds to a row in the CSV file.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the specified file is empty or contains invalid data.
        """
        # if file_path == "data\data.csv":
        list_of_stock_market_instances = []

        with open(file_path, newline="") as file:
            reader = csv.reader(file)

            # Skip header row if it exists
            if csv.Sniffer().has_header(file.read(1024)):
                file.seek(0)
                next(reader)

                if  file_path == "data\data.csv":
                    # Create Stock objects and append to list
                    for row in reader:
                        name_of_an_action = row[0]
                        share_price = int(row[1])
                        profitability_of_an_share = int(row[2])
                        stock = Stock(name_of_an_action, share_price, profitability_of_an_share)
                        list_of_stock_market_instances.append(stock)
                    return list_of_stock_market_instances
                else:
                    # Create Stock objects and append to list
                    for row in reader:
                        if float(row[1])<=0 or float(row[2]) <= 0:
                            pass
                        else:
                            name_of_an_action = row[0]
                            share_price = int(float(row[1])*100)
                            profitability_of_an_share = int(float(row[2])*100)
                            stock = Stock(name_of_an_action, share_price, profitability_of_an_share)
                            list_of_stock_market_instances.append(stock)
                    return list_of_stock_market_instances
