## @file math_lib.py
#  @brief Library containing various simple math functions
#  @author Martin Mezei
#  @author Adam Ivan
#  
#  This module provides basic arithmetic operations


##
#  @brief Adds two numbers
#
#  Function add() takes two numbers as input and adds them
#
#  @param number1 First number of addition
#  @param number2 Second number of addition
#  @return Sum of number1 and number2
def add(number1, number2):
    return number1 + number2

##
#  @brief Substracts two numbers
#
#  Function sub() takes two numbers as input and substracts them
#
#  @param number1 First number of substraction
#  @param number2 Second number of substraction
#  @return Difference of number1 and number2
def sub(number1, number2):
    return number1 - number2

##
#  @brief Divides two numbers
#
#  Function div() takes two numbers as input and divides them
#  If zero division is attempted ZeroDivisionError is raised
#
#  @param number1 Dividend
#  @param number2 Divisor
#  @return Division quotient
def div(number1, number2):

    if number2 == 0:
        raise ZeroDivisionError("Cannot divide with 0")
        
    return number1 / number2

##
#  @brief Multiplies two numbers
#
#  Function mult() takes two numbers as input and multiplies them
#
#  @param number1 First number of multiplication
#  @param number2 Second number of multiplication
#  @return Multiplication product
def mult(number1, number2):
    return number1 * number2

##
#  @brief Finds absolute value of a given number
#
#  @param number Argument of the absolute value function
#  @return Absolute value of a number
def absolute(number):

    if number < 0:
        return -number #negates number if number is negative
    else:
        return number #returns number as it is if number is positive or equal to 0

##
#  @brief Calculates factorial of a number
#
#  Function factorial() takes one number which is either 0 or a natural number and calculates its factorial
#  If a calculation with a number that is not 0 or natural is attempted ValueError is raised
#   
#  @param number Argument of factorial function
#  @return Value of factorial for the given number
def factorial(number):

    if number < 0: 
        raise ValueError("Only factorials of 0 and natural numbers")

    if type(number) is float: #checks if number is natural
        raise ValueError("Only factorials of 0 and natural numbers")

    if number == 1 or number == 0: #1! and 0! are both equal to 1
        return 1

    rValue = 1 #return value

    for currentNum in range(2,number+1): #rValue does not have to be multiplied by 1 and cannot be multiplied by 0, so for starts at 2
        rValue = mult(rValue,currentNum)

    return rValue

##
#  @brief Calculates remainder after division
#
#  Function modulo() takes two numbers and returns the remainder after division
#  As in the div() function, returns ZeroDivisionError if using modulo with 0
#
#  @param number1 First number in division
#  @param number2 Second number in division
#  @return Remainder after division
def modulo(number1, number2):
    
    if (number2 == 0):
        raise ZeroDivisionError("Modulo by zero is not allowed")
    
    return number1%number2

##
#  @brief Calculates the natural power of number
#
#  Function n_power() takes two numbers and calculates number1 to the power of number2
#  This function raises ValueError if not using natural numbers in exponents
#
#  @param number1 Base of exponentiation
#  @param number2 Exponent of exponentiation
#  @return Value of nth power for the given numbers
def n_power(number1, number2):

    if number2 < 0: 
        raise ValueError("The exponent n must be a natural number, or 0")

    if type(number2) is float: #checks if number is natural
        raise ValueError("The exponent n must be a natural number, or 0")
    
    return number1**number2

##
#  @brief Calculates the natural root  of number
#
#  Function n_root() takes two numbers and calculates the number2 root of number1
#  This function raises ValueError if not using natural numbers in the exponents of root
#
#  @param number1 Radicand of root
#  @param number2 Degree of root
#  @return Value of nth root for the given numbers
def n_root(number1, number2):

    if number2 <= 0: 
        raise ValueError("The exponent n must be a natural number")

    if type(number2) is float: #checks if number is natural
        raise ValueError("The exponent n must be a natural number")
    
    return number1**(1/number2)
