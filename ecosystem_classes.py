import random
import pylab
import numpy

class Animal(object):

    def __init__(self, max_rabbits):
        self.max_rabbits = max_rabbits
        self.foxes_list = []
        self.rabbits_list = []

    def steps_method(self, animal):
        for i in range(self.steps):
            return self.run_simulation(animal)


class Rabbits(Animal):

    def __init__(self, rabbits_pop, max_rabbits):
        Animal.__init__(self, max_rabbits)
        self.rabbits_pop = rabbits_pop

    def rabbit_probability(self):
        for i in range(self.rabbits_pop):
            if random.random() < 1 - float(self.rabbits_pop) / self.max_rabbits:
                self.rabbits_pop += 1

class Foxes(Rabbits):

    def __init__(self, rabbits_pop, foxes_pop, max_rabbits):
        Rabbits.__init__(self, rabbits_pop, max_rabbits)
        self.foxes_pop = foxes_pop

    def fox_probability(self):
        for i in range(self.foxes_pop):
            if random.random() < float(self.rabbits_pop)/self.max_rabbits and self.rabbits_pop > 10:
                self.rabbits_pop -= 1
                if random.random() <= 0.3:
                    self.foxes_pop += 1
            elif random.random() >= 0.1 and self.foxes_pop > 10:
                self.foxes_pop -= 1

class Run(object):

    def time_step(self, obj):
        obj.rabbit_probability()
        obj.fox_probability()
        obj.foxes_list.append(obj.foxes_pop)
        obj.rabbits_list.append(obj.rabbits_pop)

    def run_simulation(self, steps, obj):
        for i in range(steps):
            self.time_step(obj)

    def visualisation(self, list_of_populations, dotes_atribute, line_atribute):
        coeff = numpy.polyfit(range(len(list_of_populations)),list_of_populations,2)
        pylab.plot(range(len(list_of_populations)),list_of_populations,dotes_atribute)
        pylab.plot(numpy.polyval(coeff,range(len(list_of_populations))),line_atribute)


fox = Foxes(500, 30, 1000)
run = Run()
run.run_simulation(50, fox)
run.visualisation(fox.rabbits_list, 'go', 'g')
run.visualisation(fox.foxes_list, 'ro', 'r')
pylab.show()
