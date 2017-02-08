while True:
    print("Welcome to the leap year tester\n===============================")
    year = int(input("\nEnter the year: "))
    divisibale_by_4 = year % 4
    counter = 0
    x = 0
    divisibale_by_400 = year % 400
    divisibale_by_100 = year % 100
    if divisibale_by_4 == 0:
        x = 1 


    else:
        print("\nThis is not a leap year\n")
        counter = 1

    if counter < 1:
     

        if divisibale_by_100 > 0 :
            print("\nLeap year\n")
            counter = 1

        if divisibale_by_100 == 0:
            x = 1

        if counter < 1:


            if divisibale_by_400 == 0:
                print("\nThis is a leap year3\n")

            else:
                print("\nThis is not a leap year\n")

    counter = 0

