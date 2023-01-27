a = int(input("Enter number?"))
fib = [1,2]
for i in range(2,a) :
    b = fib[i-1] + fib[i-2]
    fib.append(b)
print(fib)