p=open("happy_no.txt")
l=[]
happy=p.read()
q=open("prime_n.txt")
prime=q.read()
list_happy=happy.split(",")
list_prime=prime.split(",")
for i in list_happy:
    if i in list_prime:
        l.append(i)
    else:
        continue
str1=",".join(l)    
print("Matching Values in happy no. and prime no.")
print(str1)

