# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:14:32 2020

@author: Izagma
"""

# Clyde "Thluffy" Sinclair
# Aug 2020

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n

def fib(n):
    if n == 1:
        return 1
    else:
        return n-1+n

n = 5
factorial(n)
print(n)

print("Good News Everyone!")
print(f"1! = {factorial(1)}" )
print(f"2! = {factorial(2)}" )
print(f"3! = {factorial(3)}" )
print(f"10! = {factorial(10)}" )
print(f"fib(1) = {fib(1)}" )
print(f"fib(2) = {fib(2)}" )
print(f"fib(3) = {fib(3)}" )