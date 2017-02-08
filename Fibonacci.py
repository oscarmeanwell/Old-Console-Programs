while True:
    print("\nFibonacci sequence\n==================")
    upto = int(input("\nEnter a limiting value: "))
    print() # Prints new line to add spacing
    a = 1 # Temp variable to hold number
    b = 1 # Temp variable to hold number
    f = 0 # Stops loop when it has reached the input value
    counter = 2 # Counts how many number there are in the sequence
    t = [1,1] # Means list can be printed out on one line
    total = 0 # Total sum of numbers in the sequence

    while f == 0 : # Stops when it has reached upto value
        total = a + b 
        a = b
        b = total
        if total > upto: # Stops loop when values are past input
            f = 1

        else:
            t.append(total) # adds values in sequnce to list 
            counter = counter + 1 # Tracks how many terms there are

    counter2 = 0 # define new counter to help with list printing

    while counter2 != counter :
        print(t[counter2], end=' ')
        counter2 = counter2 + 1 # prints out sequence all on one line

            
            
    print("\n\nThere are" , counter , "terms up to" , upto) # lists amount of terms

