a=int(input("enter a number between 1 and 6: "))
match a:
    case 1:
        print("case is one")
    case 2:
        print("case is two")
    case 3:
        print("case is 3")
    case 4:
        print("case is 4")
    case 5:
        print("case is 5")
    case 6:
        print("case is 6")
    case _: #this _ is used for default for refer in switch case.
        print("no match found")