
def create_stock(symbol, value=1, total_shares=100, sold_shares=0):
    return dict(locals())


def sell(stock, shares):
    new_shares = stock['sold_shares'] - shares

    if new_shares < 0:
        raise Exception("Cannot sell more shares than exist")
    else:
        stock['sold_shares'] = new_shares


def buy(stock, shares):
    new_shares = stock['sold_shares'] + shares

    if new_shares > stock['total_shares']:
        raise Exception("Cannot buy more shares than the total exist")
    else:
        stock['sold_shares'] = new_shares
