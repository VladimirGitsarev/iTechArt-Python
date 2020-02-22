# Task 1, Option 13

import random
import datetime
import math

class Bus():
    __model = 'Undefined'
    __year = 0
    __run = 0
    __models = ['MAZ', 'Ikarus', 'Volgren', 'MAN', 'Mercedes', 'NABI', 'Bogdan', 'Scania']

    @staticmethod    # Method for creating Buses with random fields
    def object_creator(name = 'Undefined', bus = '0', way = '0'):
        bus = Bus(name, bus, way)
        bus.__model = Bus.__models[random.randint(0, len(Bus.__models) - 1)]
        bus.__year = random.randint(1970, datetime.datetime.now().year)
        bus.__run = random.randint(1000 * (datetime.datetime.now().year - bus.__year),\
                    10000 * (datetime.datetime.now().year - bus.__year))
        return bus

    @staticmethod    # Method for searching buses with given way number
    def way_list(lst, num):
        check = False
        print('\nBuses with way number {}:'.format(num))
        for bus in lst:
            if bus.way_number == num:
                check = True
                print(str(bus))
        if not check:
            print('No such buses') 

    @staticmethod    # Method for searching buses older than given age
    def year_list(lst, year):
        check = False
        print('\nBuses older than {}:'.format(year))
        for bus in lst:
            if datetime.datetime.now().year - bus.__year > int(year):
                print(str(bus))
        if not check:
            print('No such buses') 

    # Сlass constructor with optional parameters (Constructor with parametrs and without them)
    def __init__(self, n = 'Undefined', b = '0', w = '0'):   
        self.name = n
        self.bus_number = b
        self.way_number = w
        print("New {} bus created!".format(self.bus_number))

    # Encapsulation implementation below using user methods for getting, setting and validating attributes

    def set_model(self, value):
        if value in self.__models:
            self.__model = value
        else:
            print("No such model: {}!".format(value))
            
    def get_model(self):
        return str(self.__model)

    def set_year(self, value):
        if value < 0:
            self.__year = 0
            print('Wrong year: {}!'.format(value))
        else:
            self.__year = value
    
    def get_year(self):
        return str(self.__year)
    
    def set_run(self, value):
        if value < 0:
            self.__run = 0
            print('Wrong run: {}!'.format(value))
        else:
            self.__run = value

    def get_run(self):
        return str(self.__run)

    def __setattr__(self, attr, value):

        if attr == '_Bus__year':
            self.__dict__[attr] = value

        if attr == '_Bus__model':
            self.__dict__[attr] = value

        if attr == '_Bus__run':
            self.__dict__[attr] = value

        if attr == 'name':
            self.__dict__[attr] = value
        
        if attr == 'bus_number':
            self.__dict__[attr] = value

        if attr == 'way_number':
            self.__dict__[attr] = value       

    def __str__(self):
        return '\nModel: ' + self.__model + ' | Year: ' + str(self.__year) + ' | Run: ' + str(self.__run) + \
               '\nDriver: ' + self.name + '\nBus number: ' + self.bus_number + '\nWay number: ' + self.way_number 

if __name__ == '__main__':
    bus_list = list()
    bus1 = Bus('John Doe', '1337 AA-2', '54')
    bus1.set_model('MAZ')
    bus1.set_year(1999)
    bus1.set_run(34234)
    bus2 = Bus.object_creator('Leonid Matveenko', '2288 AB-7', '54')
    bus3 = Bus.object_creator('Alexey Tsiabuk', '2344 AC-3', '5')
    bus4 = Bus.object_creator('Vladimir Gitsarev', '1423 AK-5', '113')
    bus5 = Bus.object_creator('Maksim Alekseev', '8433 AM-4', '8')

    del bus5
    del bus4
  
    bus_list.append(bus1)
    bus_list.append(bus2)
    bus_list.append(bus3)
    
    print(*bus_list)

    Bus.way_list(bus_list, input("\nEnter way number: "))
    Bus.year_list(bus_list, input("\nEnter age: "))

