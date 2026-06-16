from dataclasses import dataclass

@dataclass
class DataC:
    a : str = "The answer to the life the universe and everything"
    b : int = 42

    def __post_init__(self):
        assert isinstance(self.a, str), "Attribute a is not a string"
        assert isinstance(self.b, int), "Attribute b is not an integer"


d = DataC()

e = DataC(42, 'b')
