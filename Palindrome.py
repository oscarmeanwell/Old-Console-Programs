while True:
    print("\nWelcome to the Palindome tester!\n================================")
    word = input("\nEnter a word: ")
    print()
    topindex = 0
    for i in range(1, len(word)+1):
        topindex = len(word) - i
        print("Letter ", i, "is ", word[i-1], "Letter ", topindex, " is ", word[topindex])
    if word[i - 1] == word[topindex]:
        print("\nIs a Palindrome!")

    else:
        print("\nNot a Palindrome!")

    again = input("\nWant to use this tool again? y/n: ")
    if again == 'n' or again == 'N':
        break

    else:
        topindex = 0
    
