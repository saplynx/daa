'''
Recursive and Non-recursive fibonacci program
'''

def RecursiveFibonacci(n):
    if n <= 0:
        return "Invalid input"
    
    if n == 1:
        return 1
    
    if n == 2:
        return 1
    
    return RecursiveFibonacci(n-1) + RecursiveFibonacci(n-2)

def NonRecursiveFibonacci(n):
    if n <= 0:
        return "Invalid input"
    
    if n == 1:
        return 1
    
    if n == 2:
        return 1
    
    fib1 = 1
    fib2 = 1
    fib3 = 0
    for i in range(3, n+1):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
    return fib3

def main():
    n = int(input("Enter a number: "))
    for i in range(1, n+1):
        print(RecursiveFibonacci(i))

main()
