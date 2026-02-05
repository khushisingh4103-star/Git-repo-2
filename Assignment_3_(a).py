n = int(input("Enter a number: "))

def fac(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

f = fac(n)
print(f"Factorial of {n} is: {f}")
