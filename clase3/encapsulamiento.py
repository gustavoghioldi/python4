class Car:
    def __init__(self, color, model, max_speed, cost):
        self.__color = color
        self.__model = model
        self.max_speed = max_speed
        self.cost = cost+(cost*0.21)
    
    def set_color(self, new_color, cost): #set cuando voy a cambiar un valor
        self.__add_cost(cost)
        self.__color = new_color

    def __add_cost(self, new_cost): #add cuando voy a gregar un valor
        self.cost += new_cost +(new_cost*0.21)

    def get_color(self): # cuando voy a retornar un valor
        return self.__color

    def get_model(self):
        return self.__model

    def del_cost(self):
        self.cost = 0    

#del cuando voy a borrar un valor     
car1 = Car("red", 2015, 180, 1000000)

car1.set_color("blue", 100)

print(f"color del auto: {car1.get_color()} y costo {car1.cost}")
# esto da error
# car1.__color 