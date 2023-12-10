#here we can see yell function taking only one parameter
#how about 2 or 3 or 4 or many?
#============================================
# def main():
#     yell("this is CS50")
    
# def yell(phrase):
#     print(phrase.upper())
    

# if __name__=="__main__":
#     main()
#=======================
#it can be done with list?
# def main():
#     yell("this", "is", "cs50")

# def yell(words):
#     uppercased=[]
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)

# if __name__=="__main__":
#     main()
#=================================
#more user friendly?

# def main():
#     yell("this", "is", "cs50")

# def yell(*words):
#     uppercased=[]
#     for word in words: 
#         uppercased.append(word.upper())
#     print(*uppercased)

# if __name__=="__main__":
#     main()
# ==============================================
# do it with map!?

def main():
    yell("this", "is", "cs50")

def yell(*words):
    uppercased=map(str.upper, words)
    print(*uppercased)

if __name__=="__main__":
    main()

