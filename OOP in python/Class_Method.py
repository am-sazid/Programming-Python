class Person :
    name = "Sazid"
    
    @classmethod
    def change_name(cls,name):
        cls.name = name
        
p1 = Person()
p1.change_name("AM Sazid")
print(p1.name)