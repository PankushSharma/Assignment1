class Game_toe():
    def __init__(self):
        game=[[[] for i in range(3)] for i in range(3)]
        for i in range(3):
              for j in range(3):
                number=int(input("move by player 1 or 2 "))
                if number==0:
                    print("cell not flled by any player")
                game[i][j]=number
        print(game,end=" ")
        flag=0
        for i in range(0,2):
                if game[i][0]==game[i][1]==game[i][2]: #column
                    if game[i][0]==0:
                        continue
                    a=game[i][0]
                    print("winner is player "+str(a))
                    flag=1
                    break
                elif game[0][i]==game[1][i]==game[2][i]:  # row
                    if game[0][i]==0:
                            continue
                    b=game[0][i]
                    print("winner is player "+str(b))
                    flag=1
                    break
                elif game[0][0]==game[1][1]==game[2][2]:
                    if game[0][0]==0:
                        continue
                    c=game[0][0]
                    print("winner is player "+str(c))
                    flag=1
                    break
                elif game[0][2]==game[1][1]==game[2][0]:
                    if game[0][2]==0:
                        continue
                    d=game[0][2]
                    print("winner is player "+str(d))
                    flag=1
                    break
        if flag==0:
            print(" no winner")
a=Game_toe()
