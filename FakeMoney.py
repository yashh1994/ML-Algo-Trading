from datetime import datetime
from typing import Dict

class FakeWallet:
    def __init__(self, balance: float) -> None:
        self.balance = balance
        self.coin = ""
        self.price_of_init = 0
        self.side = "None"
        self.limit = balance
        self.date_of_creation = datetime.now()
        self.coin_quntity = 0


    def buy_coin(self, coin_symbol: str, coin_price: float, coin_quantity: float,side:str) -> None:
        if coin_price * coin_quantity > self.balance:
            raise ValueError("Insufficient balance to buy the coin.")
        else:
            self.balance -= coin_price * coin_quantity
            self.coin = coin_symbol
            self.price_of_init = coin_price
            self.coin_quntity = coin_quantity
            self.side = side

    def sell_coin(self, coin_symbol: str, coin_price: float, coin_quantity: float) -> None:
        if self.coin != coin_symbol:
            raise ValueError("unknown Coin")
        else:
            self.coin_quntity -= coin_quantity
            self.balance += ()

    def wallet_status(self) -> str:
        total_gain = self.balance - self.limit
        return (f"Balance is {self.balance}, coins in Wallet are {self.coin_to_number_of} "
                f"with Total Gain of {total_gain}, wallet created on {self.date_of_creation}")

    def current_value(self, current_prices: Dict[str, float]) -> float:
        total_value = self.balance
        for coin, quantity in self.coin_to_number_of.items():
            total_value += quantity * current_prices.get(coin, 0)
        return total_value

    def is_open_position(self,symbol):
        if symbol in self.coin_to_number_of:
            return self.coin_to_number_of[symbol] != 0
        return False