registry = []

def register(func):
    print(f'running register({func})')
    registry.append(func)
    def trick():
        print(f'Haha I replaced your function named: {func.__name__}!')
    return trick

@register
def f1():
    #When decorated variable f1 is now bound to trick() instead i.e. f1 = trick
    print('running f1')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__== '__main__':
    main()