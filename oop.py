class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
            print(f"Hello, my name is {self.name} and my age is {self.age}")
#creating my object
person1=person("Lynton",19)
person1.say_hello()
person2=person("Ethan",32)
person2.say_hello()
person3=person("Mark",12)
person3.say_hello()
person4=person("Carlos",17)
person4.say_hello()
person5=person("Jones",20)
person5.say_hello()
#create a class called cars with the following attributes/properties
#make,model,year then create a function that prints make, model and year
#then create three objects
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def this_car(self):
        print(f"This car is a {self.make} model {self.model} and was manufactured in {self.year}")

car1=car("Toyota","Luxel",2013)
car1.this_car()
car2=car("Cadilac", "Escalade", 2020)
car2.this_car()
car3=car("Audi", "R8", 2010)
car3.this_car()
class song:
    def __init__(self, song, artist):
        self.song = song
        self.artist = artist
    def this_album(self):
        print(f"The song {self.song} by {self.artist} is arguably one of the best songs ever")

song1=song("R.I.C.O","Drake & Meek Mill")
song1.this_album()
