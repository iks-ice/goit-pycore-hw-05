def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        nonlocal cache
        if n <= 0:
            return 0
        if n == 1:
            return 1
        key = str(n)
        if key not in cache:
            cache[key] = fibonacci(n - 1) + fibonacci(n - 2)
            
        return cache[key]
    return fibonacci

fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610




