class Sample():
    __count = 0
    def __init__(self):
        self.__count += 1
    def __del__(self):
        self.__count -= 1

class Table():
    def __init__(self, w):
        self.weight = w

class Truck():
    __weight = 0
    def __init__(self):
        self.cur_weight = 0
        self.cargo = []

    def set_weight(self, w):
        self.__weight = w
    
    def get_weight(self):
        return self.__weight 
   
    def add_cargo(self, table):
        if self.__weight - (self.cur_weight + table.weight) > 0:
            self.cur_weight += table.weight
            self.cargo.append(table.weight)
            print("Space left:", self.__weight - self.cur_weight)
        else:
            print("You can't add anymore")

    def __str__(self):
        return(str(self.cargo))


if __name__ == '__main__':
    myTruck = Truck()
    myTruck.set_weight(100)
    print("Weight:", myTruck.get_weight())

    
    myTruck.add_cargo(Table(13))
    #myTruck.addCargo(Table(54))
    #myTruck.addCargo(Table(19))
    #myTruck.addCargo(Table(43))



    