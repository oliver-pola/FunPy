# (not efficient) prime factorization
# based on same principle as my FizzBuzz solution

n = 100
primes = []

for i in range(2, n+1):
    divisors = []
    for p in primes:
        if i % p == 0:
            divisors.append(p)
    if len(divisors) > 0:
        print(divisors)
    else:
        print(i)
        primes.append(i)
