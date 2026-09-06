from tombola import Tombola

class Fake(Tombola):
    def pick(Self):
        return 13

f= Fake()