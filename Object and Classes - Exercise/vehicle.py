class Vehicle:
    def __init__(self, type1, model, price):
        self.type1 = type1
        self.model = model
        self.price = price
        self.owner = "None"

    def buy(self, money: int, owner: str):
        if self.owner != "None":
            "Car already sold"
        elif money < self.price:
            return "Sorry, not enough money"
        else:
            change = money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type1}.Change: {change}"

    def sell(self):
        if self.owner != "None":
            self.owner = "None"
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner != "None":
            return f"{self.model} {self.type1} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type1} is on sale: {self.price}"


new_vehicle = Vehicle("truck", "Mercedes", 35000)
print(new_vehicle.buy(16000, "Ivan"))
print(new_vehicle.buy(40000, "Peter"))
print(new_vehicle)
new_vehicle.sell()
print(new_vehicle)
