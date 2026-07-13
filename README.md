# Fluent Python

I am reading the book fluent python, here I practice with it's concepts or check out the behaviour of its examples. And track my progres throughout the book.

## Concept summary to be implemented?

```
## Chapter 11 – A Pythonic Object

### Main concepts
- Data model
- Dunder methods
- Alternative constructors
- Hashability

### New things I learned
- def creates a function object.
- Classes are objects too.
- __bytes__ defines a binary representation.

### Things that surprised me
- memoryview doesn't copy memory.
- cls() makes subclasses work automatically.
```

# Notes

## Chapter 1: The Python Data Model:

### Magic and Duner:

Magic method is slang for special method. "Dunder" is short for "double underscore before and after".

Special methods are used by the python intepreter. When you call ```len(my_object)``` the interpreter calls the ```my.object.__len__``` method you implemented.
The interpreter takes a shortcut for built-in types like *list, str, bytearray,* or extensions like numpy arrays which are much faster because they are written inside a C struct (a C record type with named fields). If you need to invoke a special method it's usually better to call the related built-in function, i.e. ```len, iter, str```.

Special methods are also use to define:

- Emulation of numeric types: this means specifying the behavior of operators on the object (i.e. +, -, etc.) 
- Defining the string representation of the object, i.e. when ```str()``` or ```repr()``` is called on the object.
- Defining a boolean value of a custom type.

## Chapter 7: Functions as First-Class Objects:

**Functions**: Functions in python are Objects. <br>
**Higher-Order Functions**: A higher order function is a function that takes a function (callback) as an argument. Examples of this are: map() and filter(). <br>
**Anonymous Fucntions**: Created with the ```lambda``` keyword. The body cannot cntain other Python statements (like ```while```, ```try```, etc.)

### Nine Flavors of Callable Objects:

| Flavor                 | Description                                                   |
|------------------------|---------------------------------------------------------------|
| User-defined functions | Created with ```def``` statements or ```lambda``` expressions |
| Built-in functions | A function inplemented in C, like ```len``` or ```time.strftime```
| Methods | Functions defined in the body of a class. |
| Classes | When invoked, a class runs its ```__new__``` method to create an instance, then ```__init___``` to initialize it, and finally the instance is returned to the caller. Because the is no ```new``` operator in Python, calling a class is like calling a function. |
| Class instances | If a class defines a ```__call__``` method, then its instances may be invoked as funtions. |
| Generator functions | Functions that use the ```yield``` keyword in their body. When called, the return a generator object. |
| Native coroutine functions | Functions or methods defined with ```async def```. When called, they return a coroutine object. |
| Asychronous generator functions | Functions or methods defined with ```async def``` that have yield in their body. When called they return an asynchronous generator for use with ```async for```. |

### Positional to Keyword-Only Parameters:

To specify keyword-only arguments when defining a function, name them after the argument prefixed with *. If you don't want to support variable positional arguments but still want keyword-only arguments, put a * by itself in the signature like this:

```
def f(a, *, b):
    return a, b

>>>f(a, b=2)
(1, 2)
>>>f(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1 in <module>
TypeError: f() takes 1 positional argument but 2 were given.
```

### Positional-Only Parameters:

To define a function requiring positional-only parameters, use / in the parameter list.

```
def divmod(a, b, /):
    return (a //b, a% b)
```

All arguments to the left of the / are positional-only. Afther the /, you may specifiy other arguments, which work as usual.

## Chapter 9: Decorators and Closures

**Decorator**: A decorator is a callable that takes another functions as an argument (the decorated function). A decorator may perform some processing with the decorated functions, and returns it or replaces it with another function or callable object. <br><br>
**Closures**: A closure is a function with an extended scope that encompasses variables referenced in the body of the function that are not global variables or local variables. Such variables come in from the local outer scope of an outer function that encompasses the other function. It does not matter if the function is anonymous or not, what matters is that it can access nonglobal variables that are defined outside of its body.

### Variable Lookup logic:

- If there is a global ```x``` declaration, ```x``` comes from and is assigned to the ```x``` global variable module.
- If there is a ```nonlocal``` ```x``` declaration ```x``` comes from and is assigned to the ```x``` global variable module.
- If ```x``` is a parameter or is assigned a value in the function body, then ```x``` is the local variable.
- If ```x``` is referenced but is not assigned and is not a parameter:
    - ```x``` will be looked up in the local scopes of the surrounding function bodies (nonlocal scopes).
    - If not found in surrounding scopes, it will be read from the module global scope.
    - If not found in the global scope, it will be read from ```__builtins__.__dict__```.

