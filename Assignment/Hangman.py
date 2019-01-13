#HANGMAN game
d=input("welcome to hangman Enter a Word")
a=d.lower()
c=list(a)
g=("-,"*(len(a)))
l=g.split(",")
l.remove('')
k=0
while True:
    e=input("enter the letter ")
    b=e.lower()
    if b in a:
        if k>1:
             if b in l:
                    print("letter already exists !Guess Again")
                    continue
        j=a.index(b)
        l[j]=b
        c="".join(l)
        print(c)
        k=k+1
        if a==c:
            print("Congrats !You Guess Correct Word")
            break
    else:
           print("incorrect letter")
