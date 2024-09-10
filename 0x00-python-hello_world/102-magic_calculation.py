#!/usr/bin/python3
import dis  # Import the 'dis' module, which is used to disassemble Python bytecode into a human-readable format.
def magic_calculation(a, b):  # Define a function named 'magic_calculation' that takes two arguments: 'a' and 'b'.
    return a + b  # Return the result of adding 'a' and 'b'. This is the operation that will be disassembled.
dis.dis(magic_calculation)#Disassemble the bytecode for the'magic_calculation'function and print the result.This is to see the low-level operations performed by the function.
