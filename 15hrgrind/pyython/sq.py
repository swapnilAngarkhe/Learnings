from functions import square
#without the above import the below statement will not work.

for i in range(10):
    print(f"the square of {i} is equal to {square(i)}")

print(square(5))