class Stock():
    """ Defines a Stock Object
    """
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    def get_symbol(self):
        return self.symbol

    def get_value(self):
        return self.value
