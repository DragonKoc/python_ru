total = 8
n1 = 1
n2 = n1 + 1
n3 = n1 + (n1 + 1)
n4 = (n1 + n1 + (n1 + 1))
n = ""

print(n1,n2,n3,n4)

while total < 100:
    n5 = n1 + n4 + total
    n6 = n2 + n4 + total
    n7 = n1 + n2 + n4 + total
    total = n7 + 1
    print(n5,n6,n7)
    print('№ unic theme: '+str(total))
    x = total
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)

    print(n)
    total = total + 1

print('№ unic theme: ' + str(total) +"   "+ str(n))



