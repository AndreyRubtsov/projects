def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper


@price_string
def new_price(mon):
    return mon * 0.9
