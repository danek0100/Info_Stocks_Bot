class User:
    def __init__(self, name, id, stons):
        """Constructor"""
        self.name = name
        self.id = id
        self.stons = stons


class ston:
    def __init__(self, key, start_price, high_gr, risk_gr):
        """Constructor"""
        self.key = key
        self.start_price = start_price
        self.high_gr = high_gr
        self.risl_gr = risk_gr