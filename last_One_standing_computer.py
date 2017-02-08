import random
f = 0
l = 0
p = 0
comp_score = 0
user_score = 0
while f == 0 :
    print("\nWelcome to last one looses!\n===========================")
    c = 1
    k = 7
    over = 0
    while over == 0 :
        choice = 0
        l = 0
        choice = int(input("\nTo play with a Friend enter 1, to take on the computer enter 2: "))
        while choice == 1 :
            print("\nWelcome player" , c)
            print("\nThere are" , k , "Counters left")
            player = int(input("\nHow many counters do you want to take (1 max 3 min)?: "))
            if player < 4 :
                k -= player
                if k < 0 :
                    print("IMPOSSIBLE MOVE")
                    break
                if k == 0 :
                    print("\nPlayer" , c , "Looses!")
                    over += 1
                    choice = 1000
                if c == 1 :
                    c = 2
                else:
                    c = 1      
            else:
                print("\nEnter a number between 1 and 3")       
        while choice == 2 :
            p = 2
            if l == 0 :
                l = 1
                player = int(input("\nHow many counters do you want to take (1 max 3 min)?: "))
                if player < 4 :
                    k -= player
                if k < 0 :
                    print("\nIMPOSSIBLE MOVE! Computer Wins!")
                    comp_score += 1
                    break
                if k == 0 :
                    print("\nComputer wins!")
                    over += 1
                    l = 1000
                    choice = 4
                    comp_score += 1
            if l == 1 :
                comp = random.randint(1, 3)
                l = 0
                k -= comp
                print("\nThe computer took" , comp , "Counters" , k , "Left")
                if k < 0 :
                    print("\nIMPOSSIBLE MOVE\n\nPlayer Wins!")
                    user_score += 1
                    break
                if k == 0 :
                    print("\nPlayer Wins!")
                    over += 1
                    l = 1000
                    choice = 4
                    user_score += 1
        if p == 2 :   
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tComputer Score: " , comp_score)
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tUsers Score: " , user_score)    
    ag = input("\nWant to play again? y/n?: ").upper()
    if ag == 'Y' :
        f = 0
    else:
        f = 1
