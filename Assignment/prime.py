# Program to find prime no. in range from 1 to 1000
print("list of prime no. between 1 to 1000")
a=['2']
for i in range(3,1000):
    for j in range(2,i):
        if i%j!=0:
            if j<i-1:
                continue
            elif j==i-1:
                a.append(str(i))
        else:
            break
b=",".join(a)
print(b)
stri=",".join(a)
with open("prime_n.txt",mode='w+') as h:
    h.write(stri)
            
    
