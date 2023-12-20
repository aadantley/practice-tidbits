"""
fizzBuzz: 

example function with updates as we go through the TDD cycles. This file will have the end result code, but the notes will have the steps about how we got there.

"""
import typing

# because the if statements are repeated, we made a utility function called is Multiple to separate out this logic:


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
