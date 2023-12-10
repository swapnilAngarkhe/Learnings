#continuing the map.py stuff here but more effectivly 

def main():
    yell("this", "is", "cs50")

def yell(*words):
    uppercased=map(str.upper, words)
    print(*uppercased)

if __name__=="__main__":
    main()
#======================
#using list comperhension

def main():
    yell("this", "is", "cs50")

def yell(*words):
    uppercased=[word.upper() for word in words]
    print(*uppercased)

if __name__=="__main__":
    main()