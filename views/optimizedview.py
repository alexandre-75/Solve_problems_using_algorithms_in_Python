
class OptimizedView():

    def __init__(self):
        pass

    def display_resume_investment(self, profit, actions_list, time, file_path):

        """Displays a summary of the investment, shares purchased, expected profit and execution time."""
        
        if file_path == "data\dataset1_Python+P7.csv" or "data\dataset1_Python+P7.csv":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nResume best investment :")
            print(f"\nexpected profits : {profit/10000}€\n")
            total_invested = []
            for i in actions_list:
                print(f"name : {i.name_of_an_action}, price : {i.share_price/100}€")
                total_invested.append(i.share_price/100)
            print(f"\ntotal invested : {sum(total_invested)}€")
            print(f"\nprogram execution time (seconde) : {time}")

        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\nResume best investment :")
            print(f"\nexpected profits : {profit}€\n")
            total_invested = []
            for i in actions_list:
                print(f"name : {i.name_of_an_action}, price : {i.share_price}€")
                total_invested.append(i.share_price)
            print(f"\ntotal invested : {sum(total_invested)}€")
            print(f"\nprogram execution time (seconde) : {time}")
        