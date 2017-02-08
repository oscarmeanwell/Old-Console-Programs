while True:
    print("\nWelcome to the perfect number tester!\n=====================================")
    number = int(input("\nEnter a number to test if it is perfect: "))
    counter = 1
    result = 0
    Total = 0
    while counter < number :
        result = number % counter
        if result == 0 :
            Total += counter
            counter += 1
        else:
            counter += 1
    if Total == number :
        print("\nPerfect!")

    else:
        print("\nNot Perfect... Like you!")
    
