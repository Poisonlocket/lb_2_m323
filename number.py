class Number:
    def __init__(self, value: float):
        self.value = value

    @property
    def get_value(self):
        return self.value

    def square(self) -> float:
        return self.value ** 2