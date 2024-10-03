from datetime import datetime

class FakeWallet:
    def __init__(self, balance: float, coin_symbol: str) -> None:
        self.balance = balance
        self.coin_symbol = coin_symbol
        self.price_of_coin = 0
        self.side = "None"
        self.limit = balance
        self.date_of_creation = datetime.now()
        self.coin_quantity = 0

    def buy_coin(self, coin_price: float, coin_quantity: float, order: str) -> None:
        if order == "long":
            if coin_price * coin_quantity > self.balance:
                raise ValueError("Insufficient balance to buy the coin.")
            self.balance -= (coin_price * coin_quantity)
            self.coin_quantity += coin_quantity
            self.price_of_coin = coin_price
            self.side = "long"
        elif order == "short":
            self.side = "short"
            self.balance += (coin_price * coin_quantity)
            self.coin_quantity -= coin_quantity
            self.price_of_coin = coin_price
        else:
            raise ValueError(f"Order is not defined: {order}")

    def sell_coin(self, coin_price: float, coin_quantity: float, order: str) -> None:
        if self.coin_quantity < coin_quantity:
            raise ValueError("Insufficient coin quantity to sell.")
        else:
            if order == "long":
                self.balance += (coin_price * coin_quantity)
                self.coin_quantity -= coin_quantity
                self.price_of_coin = coin_price
            elif order == "short":
                self.balance -= (coin_price * coin_quantity)
                self.coin_quantity += coin_quantity
            else:
                raise ValueError(f"Order is not defined: {order}")

    def get_pos_side(self) -> bool:
        if self.coin_quantity != 0:
            return True,self.side
        else:
            return False,None

    def status(self) -> None:
        print(f"Balance: {self.balance}")
        print(f"Coin Symbol: {self.coin_symbol}")
        print(f"Price of Coin: {self.price_of_coin}")
        print(f"Coin Quantity: {self.coin_quantity}")
        print(f"Side: {self.side}")
        print(f"Limit: {self.limit}")
        print(f"Date of Creation: {self.date_of_creation}")
