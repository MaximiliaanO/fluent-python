from vector2d_v0 import Vector2d

v = Vector2d(2,4)

print(repr(v))
print(v)

print(f'string representation: {v!s}')
print(f'repr representation: {v!r}')
print(f'Self-documenting expression test: {v=}')

print(format(v, '.3f'))
print(format(v, '.3fp'))

print("Hash:", hash(v))