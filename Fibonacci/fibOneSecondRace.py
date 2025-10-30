import time
start = time.time()

count = 0
while True:
    fib = [0, 1]
    nextnum = fib[-1] + fib[-2]
    fib.append(nextnum)
    count += 1
    if time.time() - start >= 1:
        break
print(f"You got {count:,} numbers in a second")