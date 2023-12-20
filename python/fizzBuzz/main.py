"""
fizzBuzz: 

function with updates based on the TDD cycles. 
"""
import typing


def isMultiple(value: int, mod: int):
    return (value % mod) == 0


def fizzBuzz(value: int):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)
