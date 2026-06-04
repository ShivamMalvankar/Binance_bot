from bot.client import BinanceClient


def place_market_order(
    symbol,
    side,
    quantity
):

    client = BinanceClient()

    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": "MARKET",
        "quantity": quantity
    }

    return client.place_order(params)


def place_limit_order(
    symbol,
    side,
    quantity,
    price
):

    client = BinanceClient()

    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC"
    }

    return client.place_order(params)