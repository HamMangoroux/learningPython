import sys
sys.set_int_max_str_digits(100_000_000)
fibonacci = [0, 1]
f = open("fib.txt", 'w')
f.write(f"{fibonacci[0]}\n")
f.write(f"{fibonacci[1]}\n")

#for _ in range(2, 1_000):
while True:
        nextnum = fibonacci[-1] + fibonacci[-2]
        f.write(f"{nextnum}\n")
        fibonacci.append(nextnum)
        del fibonacci[-3]
f.close()
