import argparse

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_limit_price
)

from bot.logging_config import logger


def print_order_summary(args):

    print("\n" + "=" * 40)
    print("ORDER REQUEST")
    print("=" * 40)

    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {args.side}")
    print(f"Type     : {args.type}")
    print(f"Quantity : {args.quantity}")

    if args.type.upper() == "LIMIT":
        print(f"Price    : {args.price}")

    print("=" * 40)


def print_response(response):

    print("\nORDER RESPONSE")
    print("=" * 40)

    print(
        f"Order ID      : {response.get('orderId')}"
    )

    print(
        f"Status        : {response.get('status')}"
    )

    print(
        f"Executed Qty  : {response.get('executedQty')}"
    )

    if response.get("avgPrice"):
        print(
            f"Average Price : {response.get('avgPrice')}"
        )

    print("=" * 40)

    print("\nSUCCESS")


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True
    )

    parser.add_argument(
        "--price",
        required=False
    )

    args = parser.parse_args()

    try:

        validate_side(args.side)

        validate_order_type(args.type)

        validate_quantity(args.quantity)

        validate_limit_price(
            args.type,
            args.price
        )

        print_order_summary(args)

        if args.type.upper() == "MARKET":

            response = place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )

        else:

            response = place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print_response(response)

        logger.info(
            "ORDER EXECUTED SUCCESSFULLY"
        )

    except Exception as e:

        logger.error(str(e))

        print(
            f"\nFAILED : {str(e)}"
        )


if __name__ == "__main__":
    main()