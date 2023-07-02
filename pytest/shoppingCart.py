from typing import List

class shoppingCart:
    def __init__(self, max_size:int) -> None:
        self.items : List[str] = []
        self.max_size = max_size

    def add(self, item:str):
        if self.size() == self.max_size:
            raise OverflowError("cannot add more items")
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)
    
    def getItems(self) -> List[str]:
        return self.items

    def getTotalPrice(self, price_map):
        total = 0
        for item in self.items:
            total += price_map.get(item)
        return total