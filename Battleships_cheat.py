while True:
     input("Hello! Press enter to play battleships!\n=======================================")
     print("\nBelow is a grid, this is your battleship grid\n""")
     print("""
       1 2 3 4 5 6 7 8 9
     a . . . . . . . . .
     b . . . . . . . . .
     c . . . . . . . . .
     d . . . . . . . . .
     e . . . . . . . . .
     f . . . . . . . . .
     g . . . . . . . . .
     h . . . . . . . . .
     i . . . . . . . . .""")
     print()
     print("The aim of the game is to Guess the position of the ships which are positioned\nby the computer, because im poor my battleships are only two squares long...\n""")
     ColumArray = [1,2,3,4,5,6,7,8,9]
     RowArray = [65,66,67,68,69,70,71,72,73]
     Guess = 0
     import random
     Colum = ColumArray.pop(random.randint(1,7))
     Row = RowArray.pop(random.randint(1,7))
     Row_ascii = chr(Row)
     #print("Row" , Row_ascii)
     Ship2 = Colum
     q = Colum - 1
     Ship3 = ColumArray.pop(random.randint(1,7))
     print("Ship positionn 1" , Ship2)
     print("Ship positionn 2" , q)
     while Guess < 2:
          Colum_Guess = int(input("\nEnter the Colum you think my battleship is on: "))
          Row_Guess =input("\nEnter the Row you think my battleship is on: ")
          if Colum_Guess == Ship2 or Colum_Guess == q or Colum_Guess == Ship3 and Row_ascii == Row_Guess:
              print("\nCorrect!")
              Guess = Guess + 1
          else:
              print("\nHA")            
     if Guess == 2:
      print("\nYou sunk my Battleship!")
      
