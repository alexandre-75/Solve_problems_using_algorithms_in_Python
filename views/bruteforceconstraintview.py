
class BruteForceConstraintView():

    def __init__(self):
        pass
   
    def display_best_investment(self, dictionnaire_trie):

        """Displays the information of the most profitable investment.
        Args:
        - dictionnaire_trie: a dictionary sorted in descending order of profits, 
        where the key is the name of the stock and the value is a list containing the profits, 
        number of stock market shares, invested capital, and residual capital."""

        key, values = next(iter(dictionnaire_trie.items()))
        print("\n----------------------------")
        print(f"{key}:")
        print(f"expected profit: {values[0]}€")
        print(f"number of stock market shares: {values[1]}")
        print(f"capital invested in this share: {values[2]}€")
        print(f"capital residual: {values[3]}€")
    
    def display_resume_best_investment(self, a, b, c, d, e, f):

        """Displays a summary of the best investment.
        Args:
        - a: name of the first stock market action
        - b: name of the second stock market action
        - c: number of shares of the first action
        - d: number of shares of the second action
        - e: total profit from the first action
        - f: total profit from the second action"""

        print("\nresume :")
        print(f"name financial action: {a} + {b}")
        print(f"financial stock number: {c + d}")
        print(f"total expected profits: {e + f}€")
    
    def display_program_execution_time(self, time):
        """Displays the program execution time."""
        print (f"\nthe program execution time is: {time}")
