from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.stream import TradingStream
import config


class alpaca_demo:

    @staticmethod
    def client_data():
        client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)
        account = dict(client.get_account())
        for k, v in account.items():
            print(f"{k:30}{v}")

    @staticmethod
    def show_all_open_positions():
        client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)
        positions = client.get_all_positions()
        orders = client.get_orders()

        for order in orders:
            print(order.symbol, order.qty)
        for position in positions:
            print(position.symbol, position.qty, position.market_value)

    def make_order_buy(symbol, qty):
        client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)
        order_details = MarketOrderRequest(
            symbol=str(symbol),
            qty=int(qty),
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY
        )
        client.submit_order(order_details)

    @staticmethod
    def make_order_sell(symbol, qty):
        client = TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)
        order_details = MarketOrderRequest(
            symbol=str(symbol),
            qty=int(qty),
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY
        )
        client.submit_order(order_details)

