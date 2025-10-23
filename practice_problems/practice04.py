def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def count_char(word, char):
    if not word:
        return 0
    else:
        if word[0] == char:
            return 1 + count_char(word[1:], char)
        else:
            return count_char(word[1:], char)

def print_pattern(n):
    # base case
    if n <= 0:
        return 
    print(n, end=" ")
    print_pattern(n-1)
    if n > 1:
        print(n, end=" ")


# testing
print("factorial result: ", factorial(5))
number1 = 12345
result1 = sum_of_digits(number1)
print(f"The sum of digits of {number1} is: {result1}")

n = 12
result = fibonacci(n)
print("fibonacci result:", result)

word = "recursion"
result2 = count_char(word, "r")
print("Count Char result:", result2)

num = 3
print("Print pattern result:", end=' ')
print_pattern(num)