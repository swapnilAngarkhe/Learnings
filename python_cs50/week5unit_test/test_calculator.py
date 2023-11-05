from calculator import square

def main():
    test_square()

def test_square():
    if square(2) !=4:
        print('square of 2 wasnt 4')
    if square(3) !=9:
        print('square of 3 wasnt 9')
    
if __name__=="__main__":
    main()
        