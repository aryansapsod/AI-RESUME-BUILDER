class Bike:
    def bike_info(self,model_name,price,average):
        setattr(self,"Model_Name",model_name)
        setattr(self,"Price",price)
        setattr(self,"Avarage",average)

    def bike(self):
        print(f'Model_name =',{getattr(self,"Model_Name")})
        print(f"Price= ",{getattr(self,"Price")})
        print(f"Avarage= ",{getattr(self,"Avarage")})
        print('_'*30)
bike1=Bike()
bike2=Bike()
bike1.bike_info('KTM',230890,45)
bike2.bike_info('KTM2.0',230000,40)


bike1.bike()
bike2.bike()



