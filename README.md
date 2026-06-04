# Binance Futures Testnet Trading Bot

## Features

- Market Orders
- Limit Orders
- BUY and SELL support
- CLI arguments
- Logging
- Validation
- Error Handling

## Installation

pip install -r requirements.txt

## Configure

Create .env file:

API_KEY=
API_SECRET=

## Run

python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
