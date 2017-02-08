while True:
    print("\n\nWelcome to the Multiplication table!\n====================================")
    upto = int(input("\nEnter what number you want to go up to? Must be between 1 and 9: "))
    print()
    counter = 0
    while upto in range(1,10) and counter == 0 :

        for x in range(1,upto + 1) :
            if x == 1:
                print("  " , x , end="")

            if x == 2:
                print(" " , x , end="  ")

            if x > 2:
                print(x , end="  ")
                
        for l in range(1,upto + 1) :
            print()
            print(l, end=' ')
            
            for i in range(1,upto + 1) :
                mulit = l * i
                leng = str(mulit)
                leng2 = len(leng)
                
                if leng2 > 1:
                    print("" , mulit, end="")

                else:
                    print("" , mulit, end=" ")
                    
        
        
        counter = 1

    if upto < 1 or upto > 9 :
            print("\nNumber must be between 1 and 9!")
     
 





   
    

        

            
    
 
   
    
    



   
    
