"""
Test Suite for fizzBuzz function
"""


import pytest
from main import fizzBuzz


def CheckFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal


def test_returns1With1PassedIn():
    CheckFizzBuzz(1, "1")


def test_returns2With2PassedIn():
    CheckFizzBuzz(2, "2")


def test_returnsFizzWith3PassedIn():
    CheckFizzBuzz(3, "Fizz")


def test_returnsBuzzWith5PassedIn():
    CheckFizzBuzz(5, "Buzz")


def test_returnsFizzWith6PassedIn():
    CheckFizzBuzz(6, "Fizz")


def test_returnsBuzzWith10PassedIn():
    CheckFizzBuzz(10, "Buzz")


def test_returnsFizzBuzzWith15PassedIn():
    CheckFizzBuzz(15, "FizzBuzz")
