class Student:
    def __init__ (self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
    @property
    def percentage (self):
        return str((self.phy + self.chem + self.math ) / 3) + "%"
    
stu1 = Student(99,98,97)
print(stu1.percentage)    
stu1.math = 87
print(stu1.percentage)