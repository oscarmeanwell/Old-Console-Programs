Choice = ''
Break = True
def Menu():
    global Choice
    while Choice != 1 and Choice != 2 and Choice != 3:
        print('\nWelcome to Binary to Hex!\n=========================\n')
        Choice = int(input('Do you want to convert Binary to Hex (1) or Hex to Binary (2) or quit (3)?: '))

def BinaryToHex():
    Array = []
    Hex = ''
    Breaker = True
    Count = 0
    Temp = ''
    Counter = 0
    Sum = 0
    Flag = 0
    Binary = ''
    Cont = True
    while Cont:
        Flag = 0
        Binary = input('\nPlease enter your binary: ')
        for Char in Binary:
            Stripped = Char.strip()
            if Stripped != '0' and Stripped != '1':
                Flag = 1
        if Flag == 1:
            print()
            print('Please enter a valid binary number!')
        else:
            Cont = False
    for Line in Binary:
        Temp += Line
        Count += 1
        Counter += 1
        if Count == 4 or Counter == len(Binary):
            Array.append(Temp)
            Temp = ''
            Count = 0
    Count = 0
    for Line in Array:
        Sum = 0
        Count = 0
        String = Line
        for Char in String:
            if Char == '1' and Count == 0:
                Sum += 8
            if Char == '1' and Count == 1:
                Sum += 4
            if Char == '1' and Count == 2:
                Sum += 2
            if Char == '1' and Count == 3:
                Sum += 1
            Count += 1
        if Sum == 10: Hex += 'A' 
        elif Sum == 11: Hex += 'B'
        elif Sum == 12: Hex += 'C'   
        elif Sum == 13: Hex += 'D'  
        elif Sum == 14: Hex += 'E'
        elif Sum == 15: Hex += 'F'    
        else: Hex += str(Sum)
            
    print()
    print(Binary,' in hex is ',Hex)
        
def HexToBinary():
    HexNumber = ''
    Continue = True
    Result = ''
    BinaryEquivalent = ''
    while Continue:
        Flag = 0
        HexNumber = input('\nPlease enter a hex number: ').upper()
        for Char in HexNumber:
            if Char not in ['','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F']:
                Flag = 1
                print('\nPlease enter a valid hex Number!')
        if Flag == 0:
            Continue = False
    
    for ThisHexDigit in HexNumber:
        if ThisHexDigit == '0': BinaryEquivalent = '0000'
        elif ThisHexDigit == '1': BinaryEquivalent = '0001'
        elif ThisHexDigit == '2': BinaryEquivalent = '0010'
        elif ThisHexDigit == '3': BinaryEquivalent = '0011'
        elif ThisHexDigit == '4': BinaryEquivalent = '0100'
        elif ThisHexDigit == '5': BinaryEquivalent = '0101'
        elif ThisHexDigit == '6': BinaryEquivalent = '0110'
        elif ThisHexDigit == '7': BinaryEquivalent = '0111'
        elif ThisHexDigit == '8': BinaryEquivalent = '1000'
        elif ThisHexDigit == '9': BinaryEquivalent = '1001'
        elif ThisHexDigit == 'A': BinaryEquivalent = '1010'
        elif ThisHexDigit == 'B': BinaryEquivalent = '1011'
        elif ThisHexDigit == 'C': BinaryEquivalent = '1100'
        elif ThisHexDigit == 'D': BinaryEquivalent = '1101'
        elif ThisHexDigit == 'E': BinaryEquivalent = '1110'
        elif ThisHexDigit == 'F': BinaryEquivalent = '1111'
        Result += BinaryEquivalent
    print()
    print(HexNumber, ' in Binary is ', Result)
        
if __name__ == '__main__':
    while Break:
        Menu()
        if Choice == 1:
            BinaryToHex()
            Choice = ''
        elif Choice == 2:
            Choice = ''
            HexToBinary()
        elif Choice == 3:
            Break = False
        
