__author__ = 'tuan'


class myMethod:
    greeting = ""

    def __init__(self, name="there"):
        self.greeting = name + "!"

    def sayHello(self):
        print "Hello {0}".format(self.greeting)


myInstance = myMethod()
myInstance.sayHello()
myInstance = myMethod("Tuan")
myInstance.sayHello()