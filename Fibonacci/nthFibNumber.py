fib = [0,1]
n = int(input("Which Fibonacci number do you want? "))

while len(fib) <= n :
    nextnum = fib[-1] + fib[-2]
    fib.append(nextnum)
print(fib[n])