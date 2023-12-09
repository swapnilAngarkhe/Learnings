# MEOWS=3

# for _ in range(MEOWS):
#     print("meow")
    
#typically described at the top of the code so that in case in need of any change you can direcvtly scroll up and change accordingly
#AND ALSO CONSTANT ARE WRITTEN IN "ALL CAPS"


class Cat:
    MEOWS=3
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat=Cat()
cat.meow()