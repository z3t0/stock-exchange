from enum import Enum

class Order:
    """Contains information about each order that will be or has already been processed.
    """
    def __init__(self, profile, stock, order_type, shares):
        self.profile = profile
        self.stock = stock
        self.order_type = order_type
        self.shares = shares

        self.status = OrderStatus.NOT_PROCESSED

    
    def value(self):
        """Returns the value of this order in dollars.

        This is computed by multiplying the number of shares by the
        value of each share for the stock.
        """
        return self.shares * self.stock.value

    def process(self):
        if self.order_type == "buy":
            try:
                self.stock.buy(self)
                self.profile.buy(self)
            except:
                self.status = OrderStatus.FAILED
            else:
                self.status = OrderStatus.SUCCEEDED

class OrderStatus(Enum):
    NOT_PROCESSED = 1
    SUCCEEDED = 2
    FAILED = 3
