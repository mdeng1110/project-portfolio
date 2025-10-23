def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

# testing
print("factorial result: ", factorial(5))
number1 = 12345
result1 = sum_of_digits(number1)
print(f"The sum of digits of {number1} is: {result1}")