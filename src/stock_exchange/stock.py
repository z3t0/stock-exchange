class Stock:
    """ Defines a Stock Object
    """
    def __init__(self, symbol, value, total_shares=100):
        self.symbol = symbol
        self.value = value
        self.order_history = []
        self.total_shares = total_shares
        self.sold_shares = 0

    def _sell(self, shares):
            self.sold_shares -= shares

    def _buy(self, shares):
            self.sold_shares += shares

    def process(self, order):
        can_process = self.can_process()

        if can_process:
            if order.order_type == "sell":
                self.sell(order.shares)
            elif order.order_type == "buy":
                self.buy(order.shares)
            self.order_history.append(order)
        else:
            raise Exception("Order cannot be processed")
                
    def can_process(self, order):
        if order.order_type == "sell":
            return not (self.sold_shares - order.shares < 0)
        elif order.order_type == "buy":
            return not (self.total_shares - self.sold_shares < order.shares)
    
