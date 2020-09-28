#4
#Write Python Program to Convert Decimal to Binary, Octal and Hexadecimal and vice versa without using built in functions.
option = input('Press:1 = Decimal To Binary, Binary To Decimal,  Press:2 = \Octal To HexaDecimal HexaDecimal To Octal: ')
if option == '1':
    decimal_or_binary = input('Press: 1 = Decimal To Binary Or Press: 2 = Binary to Decimal: ')
    if decimal_or_binary == '1':
        decimal = int(input('Enter decimal: '))
        print('In Binary: {:b}'.format(decimal))
        
    if decimal_or_binary == '2':
        binary = int(input('Enter binary: '))
        print('In Decimal {:d}'.format(binary))
    
elif option == '2':
    octal_or_hexa = input('Press:1 = Octal To Hexa Or Press: 2 = Hexa To Octal: ')
    if octal_or_hexa == '1':
        octal = int(input('Enter octal: '))
        print('In Hexa(lowerCase): {:x}, (upperCase): {:X}'.format(octal,octal))
    
    if octal_or_hexa == '2':
        hexa = int(input('Enter hexa decimal: '))
        print('In Octal: {:o}'.format(hexa))

        
else:
    print('Invalid option Selected!')
