#Jitender Rajpoot

class Car:        #blueprint recipe thing called 'car'
  def __init__(self, brand, model):   #function runs when create car, carried arg brand,model
    self.brand = brand                #self allows Python keep info. separate
    self.model = model                #self-store in car;model-infor for function

  def display(self):                  #function for class
    print("This is a ", self.brand, self.model)   #

my_car = Car("Toyota", "Corolla")     #brand-Toyota;model-Corolla; create car
my_car.display()                      #call display function for output

class Cars:           #blueprint
  def __init__(self):     #what happens when car is created
    self.make = input("Enter a car brand: ")
    self.style = input("Enter the model: ")

  def display(self):
    print('This is a', self.make, self.style)

my_cars = Cars()      #use myCars blueprint to create an actual car
my_cars.display()

#collect input outside class

class Car:
  def __init__(self, make, style):
    self.make = make
    self.style = style

  def display(self):
    print('This is a ', self.make, self.style)

make = input("Enter a car brand: ")
style = input("Enter a car model: ")

my_car = Car(make, style)
my_car.display()
