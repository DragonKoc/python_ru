a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(c - 1 ,c + 1, abs(b - d))
print(d + 1 , d - 1 , abs(a - c))
if ((a == c + 1 or a == c - 1) and abs(b - d) == 2) or ((b == d + 1 or b == d - 1) and abs(a - c) ==2):
        print('YES')
else:
        print('NO')
# 2
# 8
# 3
# 7