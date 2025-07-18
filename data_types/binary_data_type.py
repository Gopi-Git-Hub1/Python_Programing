#! /usr/bin/python3

# bytes

# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)  

# Using prefix 'b' to create bytes
b2 = b'Hello'
print(b2)

# bytearray

# Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])  
print(value)  

# Creating a bytearray by encoding a string
val = bytearray("Hello", 'utf-8')
print(val)

# memoryview

data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)

import array
arr = array.array('i', [1, 2, 3, 4, 5])
view = memoryview(arr)
print(view)

data = b'Hello, world!'
# Creating a view of the last part of the data
view = memoryview(data[7:])
print(view)

