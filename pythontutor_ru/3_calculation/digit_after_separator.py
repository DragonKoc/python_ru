n = float(input())
N = int(n)

if n<1:
    n = n * 10
    n = int(n)
    print(n)
else:
    print(int(10 * (n - N)))