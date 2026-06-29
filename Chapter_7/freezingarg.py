from operator import mul
from functools import partial
import pprint

triple = partial(mul, 3)
print(triple(7))

pprint.pprint(list(map(triple, range(1, 10))))