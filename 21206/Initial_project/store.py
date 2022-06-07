from models import Product, User


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        pass

    def add_user(self, username):
        pass

    def get_total_asset(self):
        pass

    def get_total_profit(self):
        pass

    def get_comments_by_user(self, user):
        pass

    def get_inflation_affected_product_names(self):
        pass

    def clean_old_comments(self, date):
        pass

    def get_comments_by_bought_users(self, product):
        pass