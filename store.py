import products


class Store:
    def __init__(self, products):
        """Initialize the store with a list of products."""
        self.products = products

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store if it exists."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """Return a list of all active products."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """
        Accepts a shopping list of (Product, quantity) tuples.
        Buys the products and returns the total cost.
        """
        total_cost = 0
        for product, qty in shopping_list:
            total_cost += product.buy(qty)
        return total_cost

