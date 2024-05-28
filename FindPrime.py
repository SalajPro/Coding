def get_prime_factors(number):
    factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

# Input a number from the user
while True:
    try:
        number = int(input("Enter a number (or enter 0 to exit): "))
        if number == 0:
            break
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            factors = get_prime_factors(number)
            print(f"{number} is not a prime number.")
            print("Prime factors:", factors)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
