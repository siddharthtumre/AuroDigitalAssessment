import xml.etree.ElementTree as ET
from order import Order, OrderBook

def main():
    # parse xml
    tree = ET.parse("orders.xml") 
    root = tree.getroot()

    order_books = OrderBook()

    # get information about each order and add them to order_book
    for ele in root:
        book = ele.get("book")
        operation = ele.get("operation")
        price = ele.get("price")
        volume = ele.get("volume")
        order_id = ele.get("orderId")

        # Create a 
        order = Order(book=book, operation=operation, price=price, volume=volume, order_id=order_id)
        if order.book not in order_books.orders:
            order_books.add(order)



if __name__ == "__main__":
    main()