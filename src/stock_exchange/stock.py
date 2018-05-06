class Stock:
    """ Defines a Stock Object
    """
    def __init__(self, symbol, value, total_shares=100):
        self.symbol = symbol
        self.value = value
        self.order_history = []
        self.total_shares = total_shares
        self.sold_shares = 0

    def sell(self, shares):
        if self.sold_shares - shares < 0:
            raise Exception("Cannot sell more shares than currently sold")
        else:
            self.sold_shares -= shares

    def buy(self, shares):
        if self.total_shares - self.sold_shares < shares:
            print("Error: cannot buy more shares than exist")
        else:
            self.sold_shares += shares
        
