class Person: #Class created
    def checkage(self,age):
        self.age = age
        if self.age <= 0:
            print("Age is not Valid")

    def old(self, age1):
        self.age1 = age1
        if self.age1 >= 20:
            print("You are old")
    def young(self, age2):
         self.age2 = age2
         if self.age2 <=10:
             print("You are Young")
    def teen(self,age3):
        self.age3 = age3
        if self.age3 > 10 and self.age3 <= 19:
            print("You are Teenagerr")


p = Person()
print("Enter your Age to check your status: ")
i = int(input())
p.checkage(i)
p.old(i)
p.young(i)
p.teen(i)

