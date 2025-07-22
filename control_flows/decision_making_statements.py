#! /usr/bin/python3


marks = int(input('Enter the marks:'))
result = ""
if marks < 35:
   result = "Failed"
elif marks > 75:
   result = "Passed with distinction"
else:
   result = "Passed"

print(result)
