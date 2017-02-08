while True:
    print("Welcome to the prime number tester!\n===================================")
    number = int(input("\nEnter a number: "))
    counter = 1
    result = 0
    factor = 1
    while counter < number:
        result = number % counter
        if result == 0:
         factor += 1
         counter += 1
        else:
            counter += 1
    if factor == 2:
        print("\nThe number is prime!!!\n")
     
    else:
        print("\nNot Prime\n")
