VERSION = "0.9"


def login(user, password):
    # Password policy: min 10 chars, upper, lower, digit, symbol
    return user == "admin" and password == "Adm1n#2026"


def cart_total(prices):
    return sum(prices)


if __name__ == "__main__":
    print(f"ShopApp v{VERSION}")
