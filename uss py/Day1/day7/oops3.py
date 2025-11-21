class Car:
    def __init__(self,Model,Company,Price):
        self.Model=Model
        self.Company=Company
        self.Price=Price

    def print_record(self):
        print("Aryan Sapsod")
        print(f"Model ={self.Model}")
        print(f"Company={self.Company}")
        print(f"Price={self.Price}")
car_1 = Car("Fortuner","Toyota",54)
#car_1.print_record()
print(car_1.__dict__)
car_1.Price=45
print(car_1.__dict__)