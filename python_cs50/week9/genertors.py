
#=======================================
#without genertors.py
#here if we put 10000 or mroe as input the program will crsh


def main():
    n=int(input("whats the number of sheeps? "))
    for s in range(n):
        print(s)
        
#=================================
# def sheep(n):
#     flock=[]
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock
#===============================
#with the keyword yield
#this returns/yields one value at a time
def sheep(n):
    for i in range(n):
        yield "🐑" *i
        
if __name__=="__main__" :
     main()
    