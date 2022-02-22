# 10.01.2022
# Инкапсуляция
'''
class Test:
    def __init__(self,name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name = name
        
test = Test("Anton")
print(test.getName())
test.name = "vasja"
print(test.getName())
'''
'''
class Animal:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
        
    def getHeight(self):
        return self.height
    
    def getWeight(self):
        return self.weight

animal = Animal(200,400)
animal.height = 500
print(animal.getHeight())
animal.weight = 40000
print(animal.getWeight())


class Animal:
    def __init__(self,height,weight):
        self.height = height
        self.__weight = weight
        
    def getHeight(self):
        return self.height
    
    def getWeight(self):
        return self.__weight

animal = Animal(200,400)
animal.height = 500
print(animal.getHeight())
animal.weight = 40000
print(animal.getWeight())


class Animal:
    def __init__(self,height,weight):
        self.height = height
        self.__weight = weight
        
    def getHeight(self):
        return self.height
    
    def getWeight(self):
        return self.__weight
    
    def setWeight(self,weight):
        self.__weight = weight

animal = Animal(200,400)
animal.height = 500
print(animal.getHeight())
animal.weight = 40000
print(animal.getWeight())
animal.setWeight(50000)
print(animal.getWeight())
'''
'''
# Разработайте класс Earth с "полной инкапсуляцией". У этого класса должны быть следующие атрибуты:
# emissions, population, forests. Сделать так, что бы мы могли обращаться и изменять соответствующие
# атрибуты только обращаясь к определенным методам. (гетерам и сеттерам).Например, get_emissions и set_emissions.

class Earth:
    def  __init__(self,emissions,population,forests):
        self.__emissions = emissions
        self.__population = population
        self.__forests = forests
        
    def getEmissions(self):
        return self.__emissions
    def setEmissions(self,emissions):
        self.__emissions = emissions
    
    def getPopulation(self):
        return self.__population
    def setPopulation(self,population):
        self.__population = population
    
    def getForests(self):
        return self.__forests
    def setForests(self,forests):
        self.__forests = forests

earth = Earth('5,4 млн. тонн CO2.',70000000,'38 млн. км')
print(earth.getEmissions())
print(earth.getPopulation())
print(earth.getForests())
print()


earth.setEmissions('1,2 млн. тонн CO2.')
print(earth.getEmissions())
earth.setPopulation(60000)
print(earth.getPopulation())
earth.setForests('20 млн. км')
print(earth.getForests())
'''
'''
class Earth:
    def  __init__(self,emissions,population,forests):
        self.__emissions = emissions
        self.__population = population
        self.__forests = forests
    
    def __makeSomething(self):   # 1  !!!!!!!!!!!!!!!!
        print("я что-то делаю 1")
        
    def __makeMeasurementError(self):   # 2 !!!!!!!!!!!!!!!!
        return 100
        
    def getEmissions(self):
        self.__makeSomething()   # 1  !!!!!!!!!!!!!!!!
        return self.__emissions
    def setEmissions(self,emissions):
        self.__emissions = emissions
    
    def getPopulation(self):
        return self.__population
    def setPopulation(self,population):
        error = self.__makeMeasurementError()  # 2 !!!!!!!!!!!!!!!!
        self.__population = population + error  # 2 !!!!!!!!!!!!!!!!
    
    def getForests(self):
        return self.__forests
    def setForests(self,forests):
        self.__forests = forests

earth = Earth('5,4 млн. тонн CO2.',70000000,'38 млн. км')
#1 1 !!!!!!!!!!!!!!!!!!!!
print("# 1 !!!!!!!!!!!!!!!!")
#print(earth.makeSomething()) #будет ошибка
print(earth.getEmissions())  # надо так вызывать

# 2 !!!!!!!!!!!!!!!!
print()
print("# 2 !!!!!!!!!!!!!!!!")
earth.setPopulation(70000001)
print(earth.getPopulation())

#print(earth.getEmissions())
# print(earth.getPopulation())
# print(earth.getForests())
# print()
# 
# 
# earth.setEmissions('1,2 млн. тонн CO2.')
# print(earth.getEmissions())
# earth.setPopulation(60000)
# print(earth.getPopulation())
# earth.setForests('20 млн. км')
# print(earth.getForests())
'''

# Наследование
'''
class Table:
    def __init__(self, length, width, heigth):
        self.length = length
        self.width = width
        self.height = heigth

class DeskTable(Table):
    def square(self):
        return self.width * self.length
    
deskTable = DeskTable(5,7,8)
print(deskTable.square())
'''

# Создать класс mammals и унаследовать этот класс другим классом, который мы должны создать ( rhino).
# И в наследуемом классе  мы должны перевести вес животного из кг. в граммы.
'''
class Mammals:
    def __init__(self, weigth):
        self.weigth = weigth

class Rhino(Mammals):
    def kgConverter(self):
        return self.weigth * 1000

rhinoT = Rhino(789)
print(rhinoT.kgConverter())
'''
#Тоже самое, только создать новый класс Giraffe и перевести из кг в тонны
'''
class Mammals:
    def __init__(self, weigth):
        self.weigth = weigth

class Giraffe(Mammals):
    def kgConverter(self):
        return self.weigth / 1000

giraffe = Giraffe(666)
print(giraffe.kgConverter(),"тонн")
'''

class Table:
    def __init__(self, length, width, heigth):
        self.length = length
        self.width = width
        self.height = heigth
        
class DeskTable(Table):
    def square(self):
        return self.width * self.length
    
class ComputerTable(DeskTable):
    def square(self, monitor=0.0):
        return self.width * self.length - monitor

deskTable = DeskTable(0.8, 0.6, 0.7)
print(deskTable.square())

computerTable = ComputerTable(0.8, 0.6, 0.7)
print(computerTable.square(0.1))
