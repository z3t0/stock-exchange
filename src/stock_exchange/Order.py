class Order:
    """Contains information about each order that will be or has already been processed.
    """
    def __init__(self, profile, stock, order_type, shares):
        self.profile = profile
        self.stock = stock
        self.order_type = order_type
        self.shares = shares

        # True if the exchange is aware of this order
        self.processed = False
        # True if the exchange has accepted the order
        # the order may be rejected if for example the share
        # has been sold out by a previous order
        self.succeeded = False

    
    def value(self):
        """Returns the value of this order in dollars.

        This is computed by multiplying the number of shares by the
        value of each share for the stock.
        """
        return self.shares * self.stock.value
