print("Happy numbers in range from 1 to 1000")
a=[]
p=0
for i in range(1,1000):
#Happy nos. from 1 to 1000
    b=str(i)
    p=0
    if len(b)==1:
        c=str(0)+str(b)
    elif len(b)>=2:
        c=b
    for j in range(1,10):
        if j>1:
            c=str(sum1)
            if len(c)==1:
                c=str(0)+str(c)
            elif len(c)>1:
                pass
        d=int(c[0])
        sq1=d**2
        e=int(c[1])
        sq2=e**2
        sum1=sq1+sq2
        if len(c)==3:    
            f=int(c[2])
            sq3=f**2
            sum1=sum1+sq3
        if sum1==1:
            if p==0:
                p=p+1
                a.append(str(i))
                continue
            elif p==1:
                  continue
        else:
           continue
str1=",".join(a)
print(str1)
stri=",".join(a)
with open("happy_no.txt",mode='w+') as h:
    h.write(stri)
    
    
    

