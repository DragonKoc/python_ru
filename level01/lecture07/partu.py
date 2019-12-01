n1 = int(input())
n2 = int(input())
n3 = int(input())

s1 = (n1) %2
print(s1)
s2 = (n2) %2
print(s2)
s3 = (n3) %2
print(s3)
print(s1+n1)
print(s2+n2)
print(s3+n3)
t = ((s1+n1) + (s2+n2) +(s3+n3)) // 2
print (t)

