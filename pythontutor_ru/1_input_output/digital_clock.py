n = int(input())
h = ((n -(n % 60))/60) % 24
m = n - (n -(n % 60))
print (str(h) + " " +str(m))
