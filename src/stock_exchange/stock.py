class Stock:
    """ Defines a Stock Object
    """
    def __init__(self, symbol, value, total_shares=100):
        self.symbol = symbol
        self.value = value
        self.order_history = []
        self.total_shares = total_shares
