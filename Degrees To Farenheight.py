while True:
    print("\nWelcome to the degreese to farenheight convertor\n================================================")
    number = int(input("\nEnter a number: "))
    print("\nDo you want to convert this to Degrees Farenheit? If so Enter 1\nOr Degrees Centigrade?If so Enter 2")
    print("\nType and enter E at any time to Exit")
    degrees=int(input("\nEnter a choice: "))
    if degrees == 1 :
     
        result = number *9 /5+32
        print(result)
    else:
        result2 = (number-32)*5/9
        print(result2)


# °C  x  9/5 + 32 = °F

#(°F  -  32)  x  5/9 = °C
