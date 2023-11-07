# from calculator import square

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2)==4
#     except AssertionError:
#         print('square of 2 is not 4')
#     try:
#         assert square(4)==16
#     except AssertionError:
#         print('sq of 4 wasnt 16 ')
    
#         try:
#             assert square(-2)==4
#         except AssertionError:
#             print('sq of -2 wasnt 4 ')
#         try:
#             assert square(0)==0
#         except AssertionError:
#             print('sq of 0 wasnt 0 ')
    
    
# if __name__=="__main__":
#     main()
    
    
    
#-----------------------------------------

from calculator import square


def test_posetive():
    assert square(2)==4
    assert square(4)==16
    assert square(3)==9

def test_negetive():
    assert square(-2)==4 
    assert square(-3)==9
    
def test_zero():
    assert square(0)==0
    
    
        