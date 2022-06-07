from datetime import datetime
from models import Product, User


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        if product not in self.products or self.products[product] < amount:
            raise Exception("Not Enough Products")
        else:
            self.products[product] -= amount
            if self.products[product] == 0:
                del self.products[product]

    def add_user(self, username):
        if any(u.username == username for u in self.users):
            return None
        self.users.append(User(username))
        return username

    def get_total_asset(self):
        return sum([p.price * amount for p, amount in self.products.items()])

    def get_total_profit(self):
        return sum([p.price for user in self.users for p in user.bought_products])

    def get_comments_by_user(self, user):
        return [c.text for p in self.products for c in p.comments if c.user == user]

    def get_inflation_affected_product_names(self):
        return set(
            [
                p.name
                for p in self.products
                if any(
                    product
                    for product in self.products
                    if product.name == p.name
                    and product.id != p.id
                    and product.price < p.price
                )
            ]
        )

    def clean_old_comments(self, date: datetime):
        for p in self.products:
            p.comments = [c for c in p.comments if c.date_added > date]

    def get_comments_by_bought_users(self, product):
        return [
            c.text
            for u in self.users
            for p in u.bought_products
            for c in p.comments
            if c.user == u
        ]
