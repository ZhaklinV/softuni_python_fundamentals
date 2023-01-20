class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        if self.capacity > len(self.storage):
            self.storage.append(product)

    def get_products(self):
        return self.storage


input_line = int(input())
storage = Storage(input_line)
command = input()
while command != "End":
    product_name = command
    storage.add_product(product_name)
    command = input()

print(storage.get_products())
