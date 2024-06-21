
def factorize(number):
    factors = []
    divisor = 4
    
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    
    return factors

print(factorize(80))  
