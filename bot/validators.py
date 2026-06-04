valid_sides = ["BUY", "SELL"]
valid_orders = ["MARKET", "LIMIT"]


def validate_side(side):
    if side.upper not in valid_sides:
        raise ValueError(
            f"invalid state... must be one of these-> {valid_sides}"
        )


def validate_order_type(order):
    if order.upper not in valid_orders:
        raise ValueError(
            f"Invalid Order... Must be one of these-> {valid_orders}"
        )


def validate_quantity(quantity):
    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError

    except ValueError:
        raise ValueError(
            "quantity must be a positive float value."
        )


def validate_limit_price(order_type, price):
    if order_type.upper == "LIMIT":
        if price is None:
            raise ValueError(
                "price is required for limit orders"
            )
        try:
            float(price)
        except ValueError:
            raise ValueError(
                "price must be numeric"
            )

