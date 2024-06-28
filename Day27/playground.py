def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6))

def calculate(*kwargs):
    print(kwargs)

calculate(add=3, multiply=5)

calculate()
