class Stock:

    def __init__(self, name_of_an_action, share_price, profitability_of_an_share):
        self.name_of_an_action = name_of_an_action
        self.share_price = share_price
        self.profitability_of_an_share = profitability_of_an_share
        self.profit2 = (self.share_price/100)*self.profitability_of_an_share

    