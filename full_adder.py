# Logic gates and adders
def NAND(a, b):
    '''
    Truth table 
    A   B   Output
    0   0     1
    0   1     1
    1   0     1
    1   1     0
    '''
    return int(not a & b)

def NOT(a):
    '''
    Truth table 
    A   Output
    0     1
    1     0
    '''
    return NAND(a,a)

def AND(a,b):
    '''
    Truth table: &
    A   B   Output
    0   0     0
    0   1     0
    1   0     0
    1   1     1
    '''
    c = NAND(a,b)
    return NOT(c)

def OR(a,b):
    '''
    Truth table: |
    A   B   Output
    0   0     0
    0   1     1
    1   0     1
    1   1     1
    '''
    c = NOT(a)
    d = NOT(b)
    return NAND(c,d)

def XOR(a,b):
    '''
    Truth table: ^
    A   B   Output
    0   0     0
    0   1     1
    1   0     1
    1   1     0
    '''
    c = NOT(a)
    d = NOT(b)
    e = NAND(c, b)
    f = NAND(a, d)
    return NAND(e, f)

def full_adder(a,b,c):
    '''
    Truth table
    A   B   C   Sum   Output
    0   0   0    0      0
    1   0   0    1      0
    0   1   0    1      0
    1   1   0    0      1
    0   0   1    1      0
    1   0   1    0      1
    0   1   1    0      1
    1   1   1    1      1
    '''
    d = XOR(a,b)
    sum = XOR(d, c)
    f = AND(c, d)
    e = AND(a,b)
    out = OR(f,e)
    return (sum, out)

def calculate(num1, num2, addition = True): # addition and subtraction of two signed numbers
    short_binary1 = format(num1,'b')
    short_binary2 = format(num2,'b')
    max_length = len(short_binary1) + int(addition) if len(short_binary1) > len(short_binary2) else len(short_binary2) + int(addition)
    binary1, binary2 = short_binary1.zfill(max_length), short_binary2.zfill(max_length)
    if addition:
        mixed_bits = list(zip(binary1 ,binary2))[::-1]
        added_bits = ''
        carry = 0
        for bit1, bit2 in mixed_bits:
            sum, carry = adder(int(bit1), int(bit2), carry)
            added_bits += str(sum)
        answer_binary = added_bits[::-1]
        added_sum = int(answer_binary, 2)
        return added_sum
    else: # Subtraction
        if num1 < num2: 
            pseudo_negative = calculate(num2,num1, addition = False) # subtract the bigger number from the smaller 
            return (-1 * pseudo_negative) # return the result multiplied by negative 1
        else:
            two_complement = ''
            reached_one = False 
            for bit in binary2[::-1]:
                if reached_one:
                    bit = str(NOT(int(bit)))
                elif bit == '1':
                    reached_one = True
                two_complement = bit + two_complement
            two_complement_number = int(two_complement, 2)
            pseudo_minus = calculate(num1, two_complement_number, addition = True)
            answer = int(format(pseudo_minus, 'b')[1:], 2)
            return answer
