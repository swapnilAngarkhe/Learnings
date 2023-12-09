#using sys library

# import sys

# if len (sys.argv)==1:
#     print("meow")
    
# elif len(sys.argv)==3 and sys.argv[1]== "-n":
#     """here -n represents 
#     """
#     n=int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
    

# else:
#     print("usage,meows.py ")

#====================================

# using argprse lib
#argument parser (reading)

import argparse

parser=argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n", default=1, help="number of tiems to meow", type=int)
args=parser.parse_args()

for _ in range(args.n):
    print("meow")
    