__author__ = 'tuan'



# be the chance you wanna be in the world
class myMethod:
    greeting = ""

    def __init__(self, name="there"):
        self.greeting = name + "!"

    def sayHello(self):
        print "Hello {0}".format(self.greeting)


myInstance = myMethod("Tuan")
myInstance.sayHello()