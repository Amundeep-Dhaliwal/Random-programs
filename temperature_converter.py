#! python3

print('This script can be used to convert degrees fahrenheit to degrees celsius')

repeat = int(input('How many conversions do you want to do: '))

for repetition in range(repeat):
    convert = input('Please specify which unit you want to convert to (c for celsius of f for fahrenheit): ')
    if convert.isnumeric() == True:
        print('Please enter what unit you want to convert to, c or f')
    elif not convert.lower() =='c' and not convert.lower() == 'f':
        print('Please input a valid character, c or f')
    elif 'c' == convert.lower():
        num = float(input('Please input the fahrenheit value: '))
        celsius = (5/9)*(num - 32)
        print(str(num)+' degrees fahrenheit is ' + str(round(celsius, 2)) +' degrees celsius.')
    elif convert.lower() == 'f':
       number = float(input('Please input the celsius value: '))
       fahrenheit = (9/5)*(number) +32
       print(str(number)+' degrees celsius is ' + str(round(fahrenheit, 2)) +' degrees fahrenheit.')
    #else:
        #print('Sorry something went wrong')

print('Thank you for using this program and have a nice day!')
