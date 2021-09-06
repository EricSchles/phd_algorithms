from random import randint
from typing import List

def to_binary(num: int) -> List:
    num = str(bin(num))
    num = num.replace("0b", "")
    return [int(elem) for elem in num]

def equate_length(binary_number: List, bigger_length: int) -> List:
    if len(binary_number) < bigger_length:
        while len(binary_number) < bigger_length:
            binary_number.insert(0, 0)
    return binary_number

def binary_add(x: int, y: int) -> int:
    x = to_binary(x)
    y = to_binary(y)
    bigger_length = max(len(x), len(y))        
    x = equate_length(x, bigger_length)
    y = equate_length(y, bigger_length)
    # reverse to make the iteration easier
    x = x[::-1]
    y = y[::-1]
    summation = []
    carry = 0
    for index in range(len(x)):
        result = x[index] + y[index] + carry
        carry = 0
        if result == 3:
            result = 1
            carry = 1
        if result == 2:
            result = 0
            carry  = 1
        summation.append(result)
    summation.append(carry)
    return summation[::-1]

if __name__ == '__main__':

    for _ in range(1000):
        first, second = randint(0, 100000), randint(0, 100000)
        result = binary_add(first, second)
        string = ""
        for elem in result:
            string+=str(elem) 
        assert int(string, 2) == first + second
