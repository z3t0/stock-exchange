from uuid import uuid4


def create_profile(cash=100):
    profile = dict(locals())
    profile['uuid'] = uuid4()
    profile['assets'] = {}

    return profile


def buy(profile, symbol, cost, shares):
    cash_after = profile['cash'] - cost

    if cash_after < 0:
        raise Exception("Not enough cash")

    assets = profile['assets']

    if symbol in assets:
        assets[symbol]['shares'] += shares
    else:
        assets[symbol] = {}
        assets[symbol]['shares'] = shares

    profile['cash'] -= cost


def sell(profile, symbol, cost, shares):
    assets = profile['assets']
    new_shares = assets[symbol]['shares'] - shares

    if new_shares < 0:
        raise Exception("Not enough shares")

    if symbol in assets:
        assets[symbol]['shares'] -= shares
        profile['cash'] += cost
    else:
        raise Exception("Share is not owned")


def can_buy(profile, cost):
    return (profile['cash'] - cost > 0)

def can_sell(profile, symbol, shares):
    assets = profile['assets']

    if not symbol in assets:
