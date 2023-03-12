
class BruteForceView():

    def __init__(self):
        pass

    def display_best_of_the_best(self, best_of_the_best):

        """
        Prints out a summary of the best investments from a given list of investment objects.
        Parameters:
        best_of_the_best (list): A list of Investment objects representing the best investments.

        Returns:
        None

        Prints:
        A summary of the best investments including their names and share prices.
        The total profitability of all the best investments.
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nResume best investment :")
        for i in best_of_the_best:
            print(f"action : {i.name_of_an_action} - price : {i.share_price}€")
        list_sum_best_of_the_best = []
        list_sum_price = []
        for i in best_of_the_best:
            profit = (i.share_price/100) * i.profitability_of_an_share
            list_sum_best_of_the_best.append(profit)
            list_sum_price.append(i.share_price)
        total_sum_price = sum(list_sum_price)
        total_list_sum_best_of_the_best = sum(list_sum_best_of_the_best)
        print(f"\ncapital invested : {total_sum_price}€")
        print(f"\nprofitability : {total_list_sum_best_of_the_best}€")
    
    def display_execution_time(self, time):

        """Displays the execution time."""
        
        print (f"\nthe program execution time is: {time}")
