class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year =year
        self.odometer_reading = 20

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name=str(self.year) + ' '+self.make + ' '+self.model
        return long_name.title()
    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print("This car has " + str(self.odometer_reading)+ " miles on it")

    def update_odometer(self, mileage):
        '''将历程数设为指定值'''
        if mileage>self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back on odometer")
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(14)
my_new_car.read_odometer()
