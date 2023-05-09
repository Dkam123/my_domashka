print("""“Don’t compare yourself with anyone
            in this world if you do so, 
                      you are insulting yourself.”
                                       Bill Gates""")


def duo(first, second):
    for i in range(first, second + 1):
        if i % 2 == 0:
            print(i)


a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
duo(a, b)


def square(length, symbol, value):
    if value == 1:
        for i in range(length):
            if i == 0 or i == length - 1:
                print(symbol * length)
            else:
                print(f"{symbol}{' ' * (length - 2)}{symbol}")
    elif value == 2:
        for i in range(length):
            print(symbol * length)


a = int(input('length: '))
b = input('symbol: ')
v = int(input('1 - True or 2 - False: '))

square(a, b, v)



def minimal_number(a, b, c, d, e):
    lis = [a, b, c, d, e]
    print(min(lis))


first = int(input('First: '))
second = int(input('Second: '))
third = int(input('Third: '))
fourth = int(input('Fourth: '))
fifth = int(input('Fifth: '))

minimal_number(first, second, third, fourth, fifth)


def multy(a, b):
    m = 1
    if a < b:
        for i in range(a, b + 1):
            m *= i

    elif a > b:
        for i in range(b, a + 1):
            m *= i

    return m


number_1 = int(input('First: '))
number_2 = int(input('Second: '))
print(multy(number_1, number_2))



def polidorm(a):
    a = str(a)
    if a == a[::-1]:
        return True
    else:
        return False


number = int(input('Your number: '))
print(polidorm(number))