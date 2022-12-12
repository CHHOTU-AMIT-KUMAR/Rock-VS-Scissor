import random
l=['rock','scissor','paper']
'''
rock vs paper-> paper wins
rock vs scissor-> rock wins
paper vs scissor-> scissor wins
'''

while True:
    ccount=0
    ucount=0
    uc=int(input('''
    Game Start...
    1 Yes
    2 No | Exit
    '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if userInput==1:
                uchoice='rock'
            elif userInput==2:
                uchoice='scissor'
            elif userInput==3:
                uchoice='paper'
            else:
                print("invalid choice")
            cchoice=random.choice(l)
            if cchoice==uchoice:
                print("computer choice",cchoice)
                print("user choice", uchoice)
                print("game draw")
                ccount+=1
                ucount+=1
            elif ((uchoice=="rock" and cchoice=="scissor") or (uchoice=="scissor" and cchoice=="paper") or (uchoice=="paper" and cchoice=="rock")):
                print("computer choice", cchoice)
                print("user choice", uchoice)
                print("You Win")
                ucount+=1
            else:
                print("computer choice", cchoice)
                print("user choice", uchoice)
                print("Computer Win")
                ccount += 1
        print("Computer Win..",ccount)
        print("User Win:",ucount)

        print("\n\n\n....GAME RESULT.....")
        if ccount==ucount:
            print("Draw Game")
        elif ccount>ucount:
            print("Computer Win")
        else:
            print("User Win")
    else:
        break