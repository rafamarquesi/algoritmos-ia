class Person:
    population = 0 # estática
    def __init__(self, age):
        self.age = age
        Person.population += 1

    def getPopulation(self):
        return Person.population

    def getAge(self):
        return self.age