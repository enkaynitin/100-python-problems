class Person:
    name = "Person" # class name parameter

    def __init__(self, name = None):
        self.name = name    #self.name in instance parameter

Nitin = Person("Nitin")
print "{} name is {}".format(Person.name, Nitin.name)

kumar = Person()
kumar.name = "Kumar"
print "{} name is {}".format(Person.name, kumar.name)
