print("Hello, {}!".format("Pythonista"))
print("Hello, {name}! Good {moment}!".format(name="Pythonista", moment="Morning"))
print("Hello, {0}! Good {1}!".format("Pythonista", "Morning"))

""""
The Python documentation uses the following Backus–Naur form (BNF) notation to define the syntax of a replacement field for the .format() method:

replacement_field ::=  "{"
                            [field_name]
                            ["!" conversion]
                            [":" format_spec]
                       "}"

From this BNF rule, you can conclude that the field name is optional. After that, you can use an exclamation mark (!) to provide a quick conversion field. This field can take one of the following forms:

    !s calls str() on the argument.
    !r calls repr() on the argument.
    !a calls ascii() on the argument.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old."

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"
    
jane = Person("Jane Doe", 25)
print("String format: Hi! {!s}".format(jane))
print("Repr format: An instance: {!r}".format(jane))

"""
F-string BNF grammar:

replacement_field ::=  "{"
                             f_expression
                             ["="]
                             ["!" conversion]
                             [":" format_spec]
                       "}"
"""

print("f-string variants:")
print(f"String: Hi! {jane!s}")
print(f"Repr: Hi! {jane!r}")