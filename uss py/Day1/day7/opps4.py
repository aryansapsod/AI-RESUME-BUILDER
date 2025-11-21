class Car:
    def __init__(self,model,company,price):
        self.__model=model
        self.__company=company
        self.__price=price

    def print_records(self):
        print(f"Model={self.__model}")
        print(f"Company={self.__company}")
        print(f"Price={self.__price}")

car_1=Car("Hyryder","Toyota",20)
#print(car_1.__dict__)
#car_1.print_records()
car_1.price = 2.22
car_1.print_records()
