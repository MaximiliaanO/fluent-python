from dataclasses import dataclass

@dataclass
class Test:
    data : str = 'What is answer to the ultimate question of life the universe and everything?'
    other_data : str = '42'

    def print_data(self):
        print(self.data, self.other_data, sep=" ")


data = Test()
data.print_data()