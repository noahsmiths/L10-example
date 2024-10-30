def factorial(n):
    result = 0
    for i in range(n):
        result = result * i
    
    return result

print("Factorial of 5 is...", factorial(5))