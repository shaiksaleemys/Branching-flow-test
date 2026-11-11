VERSION = "1.0"


def login(user, password):
    # Password policy: min 10 chars, upper, lower, digit, symbol
    return user == "admin" and password == "Adm1n#2026"


def cart_total(prices):
    return sum(p for p in prices if p > 0)



if __name__ == "__main__":
    print(f"ShopApp v{VERSION}")


def apply_discount(total, pct):
    pct = max(0, min(pct, 100))
    return round(total * (1 - pct / 100), 2)
