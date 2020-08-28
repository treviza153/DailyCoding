#!/usr/local/bin python3
import functools
import operator


def sumList(lista):
    print(functools.reduce(operator.add, lista))
        

def numDivisible(num):
    result = [x for x in range(2, num) if num % x == 0]
    if result:
        return result
    return "Number {} is prime".format(num)

if __name__ == '__main__':
    
    lista = [1,2,3,4]
    num = 30
    sumList(lista)
    resultado = numDivisible(num)
    print(resultado)