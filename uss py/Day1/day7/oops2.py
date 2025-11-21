class Person:
    def __init__(self,name,age,city):
        print("Inside __init__ constructor")
        setattr(self,"Name",name)
        setattr(self,"Age",age)
        setattr(self,"City",city)



    def print_record(self):
        print("inside print record")
        

person1 = Person('Aryan',18,'Murud')
