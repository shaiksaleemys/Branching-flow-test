VERSION = "0.9"


def login(user, password):
    #return user == "admin" and password == "admin"
    return user == "admin" and password == "S3cure!"


def cart_total(prices):
    return sum(prices)


if __name__ == "__main__":
    print(f"ShopApp v{VERSION}")
