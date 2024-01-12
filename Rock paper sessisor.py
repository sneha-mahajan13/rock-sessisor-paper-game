import random
l=["rock","scissor","paper"]
'''
    rock vs paper --> paper wins
    scissor vs rock --> rock wins
   paper vs scissor --> scissor wins
   '''
               
while True:
    Ccount=0
    Ucount=0
    UC=int(input('''
Game start.....
1 yes|play
2 no|exit
    '''))
    if UC==1:
        for a in range(1,6):
            userInput=int(input('''
1 rock
2 scissor
3 paper
            '''))
            if userInput==1:
                Uchoice="rock"
            elif userInput==2:
                Uchoice="scissor"
            elif userInput==3:
                Uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==Uchoice:
                   print("Computer Value :",Cchoice)
                   print("User value :",Uchoice)
                   print("Game Draw")
                   Ucount=Ucount+1
                   Ccount=Ccount+1
            elif (Uchoice=="rock" and Cchoice=="scissor")or(Uchoice=="paper" and Cchoice=="rock")or(Uchoice=="scissor" and Cchoice=="paper"):
                    print("Useer value :",Uchoice)
                    print("Computer value :",Cchoice)
                    print("You win")
                    Ucount=Ucount+1
            else :
                    print("Useer value :",Uchoice)
                    print("Computer value :",Cchoice)
                    print("Computer win")
                    Ccount=Ccount+1
        if Ucount==Ccount:
                    print("Final Game Drow")
                    print("USER SCORE :",Ucount)
                    print("Computer Score :",Ccount)
        elif Ucount>Ccount:
                    print("Final you win")
                    print("USER SCORE :",Ucount)
                    print("Computer Score :",Ccount)
        else: 
                    print("Computer win the game..")                                                                  
                    print("USER SCORE :",Ucount)
                    print("Computer Score :",Ccount)
    else:
        break;           

