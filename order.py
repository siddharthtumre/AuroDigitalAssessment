import heapq

# Information about each order is stored in an object
class Order:
    def __init__(self, operation, book, price, volume, order_id):
        self.book = book
        self.operation = operation
        self.price = price
        self.volume = volume
        self.order_id = order_id

# To store buy and sell information about a particular book
class OrderBook:
    def __init__(self) -> None:
        self.orders = {}

    def add(self, order) -> None:
        self.orders["book"] = order.book
        self.orders["buyq"] = []
        self.orders["sellq"] = []