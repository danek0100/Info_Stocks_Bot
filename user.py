class User:
    def __init__(self, name, id):
        """Constructor"""
        self.name = name
        self.id = id
        self.stons = []
        self.state = 1

    def add_new_ston(self, ston):
        self.stons.append(ston)

class ston:
    def __init__(self, key, start_price, high_gr, risk_gr):
        """Constructor"""
        self.key = key
        self.start_price = start_price
        self.high_gr = start_price + start_price * (high_gr / 100)
        self.risk_gr = start_price - start_price * (risk_gr / 100)
        self.state = 0