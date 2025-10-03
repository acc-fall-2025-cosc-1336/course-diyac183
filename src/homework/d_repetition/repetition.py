def get_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

    def sum_odd_numbers(n):
        total = 0
        i = 1
        while i <= n:
            if i % 2 != 0:
                total += i
            i += 1
        return total
    
