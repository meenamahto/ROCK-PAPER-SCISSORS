import random
a=["rock","paper","scissors"]
print("let's play game.....")
while True:
    uscore=0
    cscore=0
    user_input=int(input('''
1 Yes play
2 N0| Exit    
 Enter any number:'''))
    if user_input==1:
        for i in range(1,6):
            user_choice=int(input("""
1 rock
2 paper
3 scissors        
Enter any number:"""))
            if user_choice==1:
                uchoice="rock"
            elif user_choice==2:
                uchoice="paper"
            elif user_choice==3:
                uchoice="scissors"
            cchoice=random.choice(a)

            if cchoice==uchoice:
                print("user_choise=",uchoice)
                print("computer choise=",cchoice)
                print("game draw!\n")
                uscore+=1
                cscore+=1
            elif (uchoice=='rock' and cchoice=='scissors') or (uchoice=='paper' and cchoice=='rock') or (uchoice=='scissors' and cchoice=='paper'):
                print("user_choise=",uchoice)
                print("computer choise=",cchoice)
                print("you win !\n")
                uscore+=1
            elif (uchoice=='scissors' and cchoice=='rock') or (uchoice=='rock' and cchoice=='paper')or (uchoice=='paper' and cchoice=='scissors'):
                print("user_choise=",uchoice)
                print("computer choise=",cchoice)
                print("computer win!\n")
                cscore+=1
        if uscore==cscore:
            print("final game draw...!\n")
            print("user score=",uscore)
            print("computer score=",cscore)
        elif uscore>cscore:
            print("you win the final game....!\n")
            print("user score=",uscore)
            print("computer score=",cscore)
        else:
            print("computer win the final game....!\n")
            print("user score=",uscore)
            print("computer score=",cscore)
    else:
        break









# a="c@o@d@e@i@t@u@p"
# b=a.split("@")
# print(b)
# b="".join(b)
# print(b)
