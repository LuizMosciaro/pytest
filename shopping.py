from typing import List

class ShoppingCart:
    def __init__(self,max_cart_size:int) -> None:
        self.items: List[str] = []
        self.max_cart_size = max_cart_size

    def add(self,item:str):
        if self.size() == self.max_cart_size:
            raise OverflowError('Cant add more items to cart')
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self,price_map):
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price
