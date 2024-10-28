def is_prime(func):
    def my_wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n <= 1:
            print("Составное")
        if n == 2:
            print("Простое")
        if n % 2 == 0:
            print("Составное")
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                print("Составное")
        print("Простое")
        return n

    return my_wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)