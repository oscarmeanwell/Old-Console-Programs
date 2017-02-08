print("\nWelcome to the Ancient game of Rock Paper Scissors!!!\n")
import random
from time import sleep
q = 0
users = 0
comps = 0
while q == 0:
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tComputer: " , comps)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tUser: " , users)
    choice = ['r' , 'p' , 's']
    comp = choice.pop(random.randint(0,2))
    user = input("\nEnter r for Rock, p for paper, s for scissors: ")
    print("\n\t3...")
    sleep(1)
    print("\t2...")
    sleep(1)
    print("\t1...")
    if comp == user :
        print("\nYou draw!")


    elif comp == 'r' and user == 's' :
        print("\nComputer Wins!")
        comps += 1

    elif comp == 's' and user == 'r' :
        print("\nYou win!")
        users += 1

    elif comp == 'p' and user == 'r' :
        print("\nComputer Wins!")
        comps += 1

    elif comp == 'r' and user == 'p' :
        print("\nYou win!")
        users += 1

    elif comp == 's' and user == 'p' :
        print("\nComputer Wins!")
        comps += 1

    elif comp == 'p' and user == 's' :
        print("\nYou win!")
        users += 1
    print("\nThe Computer Chose" , comp , "\n")
    again = input("\nDo you want to play again? y/n: ")
    if again == 'y' :
        q = 0

    elif again == 'n':
        print("\nFinal scores:\n " , "\nComputer: " , comps , "\nUser: " , users)
        q = 1
    
        
            

        
            
            

        
