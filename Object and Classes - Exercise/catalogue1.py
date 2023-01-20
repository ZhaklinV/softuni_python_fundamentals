class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.product_name = product_name
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        self.match_products = list(x for x in self.products if first_letter == x[0])
        return self.match_products

    def __repr__(self):
        result= f"Items in the {self.name} catalogue:\n"
        sorted_products = sorted(self.products)
        result += "\n".join(sorted_products)
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
