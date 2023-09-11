import sys

try:
    x= int(input("x: "))
    y= int(input("y: "))
except ValueError:
    print("invalid input, please enter a number")
    sys.exit(1)


try:
    result=x/y
except ZeroDivisionError:
    print("error: canot devide by 0 ")
    sys.exit(1)


print(f"{x}/{y} = {result}")
