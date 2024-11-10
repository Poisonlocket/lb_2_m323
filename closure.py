def create_multiplier(factor):
    def multiplier(x=3):
        return x * factor
    return multiplier

