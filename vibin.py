#polymorpism
class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()



#encapsulation

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


#data abstraction
# Import required modules
from abc import ABC, abstractmethod
 
# Create Abstract base class
class Car(ABC):
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
     
# Create abstract method      
  @abstractmethod
  def printDetails(self):
    pass
   
# Create concrete method
  def accelerate(self):
    print("speed up ...")
   
  def break_applied(self):
    print("Car stop")
     
# Create a child class
class Hatchback(Car):
   
  def printDetails(self):
    print("Brand:", self.brand);
    print("Model:", self.model);
    print("Year:", self.year);
   
  def Sunroof(self):
      print("Not having this feature")
     
# Create a child class
class Suv(Car):
   
  def printDetails(self):
    print("Brand:", self.brand);
    print("Model:", self.model);
    print("Year:", self.year);
   
  def Sunroof(self):
      print("Available")
 
     
car1 = Hatchback("Maruti", "Alto", "2022");
 
car1.printDetails()
car1.accelerate()








#dunder
# declare our own string class 
class String: 
	
	# magic method to initiate object 
	def __init__(self, string): 
		self.string = string 
		
	# print our string object 
	def __repr__(self): 
		return 'Object: {}'.format(self.string) 
		
	def __add__(self, other): 
		return self.string + other 

# Driver Code 
if __name__ == '__main__': 
	
	# object creation 
	string1 = String('Hello') 
	
	# concatenate String object and a string 
	print(string1 +' Geeks') 





#iterators
	
# define a list
my_list = [4, 7, 0] 

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0






## decorators argument
def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10





#decorators

def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()




#Lambda

# declare a lambda function
greet = lambda : print('Hello World')

# call lambda function
greet()


      
	


