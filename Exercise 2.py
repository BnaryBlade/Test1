def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_in_range(minimum, maximum):
    prime_numbers = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
