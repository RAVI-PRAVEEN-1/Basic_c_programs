import math

def isprime(n):
    if n <= 1:
        return False
    elif n == 2:  # 2 is the smallest prime number
        return True
    elif n % 2 == 0:  # If n is even and greater than 2, it's not prime
        return False
    # Check divisors from 3 up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

n=int(input())
print(isprime(n))
