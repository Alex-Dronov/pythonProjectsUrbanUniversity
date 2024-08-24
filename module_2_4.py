numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_not_prime = False

for i in numbers:
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                is_not_prime = True
                break

        if is_not_prime:
            not_primes.append(i)
            is_not_prime = False
        else:
            primes.append(i)

print(primes)
print(not_primes)