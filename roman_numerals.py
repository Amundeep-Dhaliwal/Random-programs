# the function below will return the string representation of a roman numeral given an integer between 1 and 3999

def intToRoman(n: int) -> str:
    ans = '' 
    numerals = {1 : 'I',
            4 : 'IV',
            5 : 'V',
            9 : 'IX',
            10 : 'X',
            40 : 'XL',
            50 : 'L', 
            90 : 'XC',
            100 : 'C',
            400 : 'CD',
            500 : 'D',
            900 : 'CM',
            1000 : 'M'}
    
    notweird = {1,2,3,5,6,7,8}
    listn = [int(x) for x in list(str(n))]
    for i in range(len(listn)):
        if listn[i] == 0:
            continue
        
        entire = (listn[i] * (10**(len(listn)-i-1)))
        
        if listn[i] == 4:
            ans += numerals[entire]
        
        if listn[i] == 9: 
            ans += numerals[entire]
        
        if listn[i] in notweird:
            
            if (10**(len(listn)-i-1)) == 1:
                five, ones = divmod(entire, 5)
                if five:
                    ans += numerals[5]
                if ones:
                    ans += numerals[1] *ones
            
            if (10**(len(listn)-i-1)) == 10:
                fifty, tens = divmod(entire, 50)
                if fifty:
                    ans += numerals[50]
                if tens:
                    ans += (numerals[10] *(int(tens/10)))
            
            if (10**(len(listn)-i-1)) == 100:
                fivehundred, hundreds = divmod(entire, 500)
                if fivehundred:
                    ans += numerals[500]
                if hundreds:
                    ans += (numerals[100] *(int(hundreds/100)))
                
            if (10**(len(listn)-i-1)) == 1000:
                ans += (numerals[1000] * listn[i])
    return ans

# a shorter version of the integer to roman numeral function (credit https://leetcode.com/patidarrohit/)

def intToRoman(self, num: int)->str:
    numlst = [1,2,3,4,5,9,10,40,50,90,100,400,500,900,1000]
    rom = ['I', 'II', 'III', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM','M']
    ans = '' 
    while num != 0:
        for i in numlst:
		if num -i >= 0:
		    div = i
        else:
                break
        q, r = divmod(num, div)
        ans += q* rom[numlst.index(div)]
        num = r
    return ans


# the function below returns the integer value for a given roman numeral between 1 and 3999

def romanToInt(s):
    ans = 0
    lists = list(s)
    numerals = { 'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    weirds = {'IV' : 4, 'IX': 9, 'XL':40, 'XC': 90 , 'CD': 400, 'CM': 900}
    for combo, value in weirds.items():
        if combo in s:
            ans += value
            s=s.replace(combo, '')
    for char in s:
        ans += numerals[char]
    return ans

# the function below uses regex to print a boolean of whether the given roman numeral is valid or not

import re
def roman_numeral_check(n):
    thousand = 'M{0,3}'
    hundred = '(C[MD]|D?C{0,3})'
    ten = '(X[CL]|L?X{0,3})'
    digit= '(I[VX]|V?I{0,3})'
    print(bool(re.match(thousand+hundred+ten+digit+'$', n)))
