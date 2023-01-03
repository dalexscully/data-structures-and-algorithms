from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

# this will need to take the animal Node, NOT the string
    def enqueue(self, animal):

        if animal.type == 'Cat':
            self.cats.enqueue(animal)
        if animal.type == 'Dog':
            self.dogs.enqueue(animal)

    def dequeue(self, pref):

        if pref.lower() == 'cat':
            return self.cats.dequeue()
        if pref.lower() == 'dog':
            return self.dogs.dequeue()
        else:
            return None


class Dog:
    def __init__(self, name='dog'):
        self.name = name
        self.type = 'Dog'


class Cat:
    def __init__(self, name='cat'):
        self.name = name
        self.type = 'Cat'
