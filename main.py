class Human:
	def __init__(self, name):
		self.name = name
		self.appearance = 5
    self.stamina = 3
    self.gladness = 5
		self.status = False
	def live(self):
		print(self.name, 'is alive')
  def ear(self):
    print("Eating time")
	def sleep(self):
		print('Sleeping time')

class Student(Human):
	def __init__(self, name):
		super().__init__()
    self.intellect = 5
		print('What a wonderful day of', self.name)
	def studying(self):
		print(self.name, 'is studying')
    self.intellect += 5
    print("Intellect:" self.intellect)
	def chilling(self):
		print(self.name, 'is chilling')
		
class Teacher(Human):
	def __init__(self, name):
		super().__init__(name)
		self.money = 20
	def work(self):
		self.money += 10
		print(self.name, 'is working')
		print('Money: ', self.money)
  def prepare(self):
    print(self.name, 'is preparing to work')


# space="-------------------------------"
# from random import *
# class Animal:
# 	def __init__(self, name):
# 		self.name = name
# 		self.homestatus = True
# 		self.appearance = 5
# 	def live(self):
# 		print('What a wonderful day of', self.name)
# 	def eat(self):
# 		print('Eating time!')
# 	def sleep(self):
# 		print('Sleeping time!')

# class Cat(Animal):
#   def claws(self):
#     print(self.name, ' is sharpen claws')
#   def wash(self):
#     print(self.name, " washed up self")
#   def longsleep(self):
#     print(self.name, " slept all day")

# class Dog(Animal):
# 	def __init__(self, name):
# 		super().__init__(name)
# 		self.stamina = 10
# 	def walk(self):
# 		self.stamina += 10
# 		print(self.name, ' go for a walk')
# 		print('Dog`s Stamina: ', self.stamina)

# class Parrot(Animal):
#   def play(self):
#     print(self.name, ' played with owner all day')
#   def fly(self):
#     print(self.name, " flew all day")

# class Snake(Animal):
#   def biteallmoving(self):
#     print(self.name, " bite all moving")
#   def hide(self):
#     print(self.name, " hide all day")
    
# animal = Animal('Animal')
# animal.live()
# print(space)
# cat = Cat('Kitty')
# live_cube = randint(1,6)
# if live_cube == 1:
#   cat.live()
# elif live_cube == 2:
#   cat.eat()
# elif live_cube == 3:
#    cat.sleep()
# elif live_cube == 4:
#   cat.claws()
# elif live_cube == 5:
#   cat.wash()
# elif live_cube == 6:
#   cat.longsleep()
# print(space)
# dog = Dog('Doggy')
# dog.live()
# dog.walk()
# dog.sleep()
# print(space)
# parrot = Parrot('Parry')
# parrot.live()
# parrot.fly()
# parrot.sleep()
# print(space)
# snake = Snake('Snack')
# snake.live()
# snake.biteallmoving()
# snake.hide()


# from random import *

# class University:
# 	def __init__(self, title, faculty):
# 		self.title = title
# 		self.faculty = faculty
# 		self.budget = False
# 	def studying(self, name):
# 		print(name, 'is studying')
# 	def isbudget(self):
# 		if self.budget == True:
# 			print('Congrats! You are on budget')
# 		else:
# 			print('Pay money and study!')

# class Student:
#   def __init__(self, name):
#     self.name = name
#     self.gladness = 50
#     self.progress = 0
#     self.money = 0
#     self.alive = True
#     self.dating = False
#   def ask_budget(self):
#     if self.progress >= 20:
#       univer.budget = True
#   def find_girl(self):
#     if self.money>=20:
#      print("*You found a girl-friend*")
#      self.dating = True
#     if self.money<20:
#       self.dating = False
#       print("You alone..")
#   def say_hello(self):
#     print('Hello!')
#   def to_work(self):
#     print('Work time')
#     self.money += 15
#     self.progress -= 5
#     self.gladness -= 10
#   def to_study(self):
#     print('Time to study')
#     if univer.budget==True:
#       self.money +=10
#     self.progress += 15
#     self.gladness -= 10
#   def to_sleep(self):
#     print('Sleep time')
#     self.gladness += 5
#   def to_chill(self):
#     print('Chill time')
#     self.money -=5
#     self.gladness += 15
#     self.progress -= 5
#   def is_alive(self):
#     if self.progress < -40:
#       print('You are bad student')
#       self.alive = False
#     elif self.gladness < 15:
#       print('Depression...')
#       self.alive = False
#     elif self.progress > 100:
#       print('Amazing!')
#       self.alive = False
#     elif self.money < -25:
#       print('Lender with experience')
#       self.alive = False
#   def statistics(self):
#     print('Gladness = ', self.gladness, ' Progress = ', self.progress, 'Money = ', self.money)
#     print('Budget = ', univer.budget)
#   def live(self, day):
#     day = 'Day ' + str(day) + ' of ' + self.name + ' life'
#     print(day)
#     live_cube = randint(1,6)
#     if live_cube == 1:
#       self.ask_budget()
#       self.to_study()
#       univer.studying(self.name)
#     elif live_cube == 2:
#       self.to_sleep()
#     elif live_cube == 3:
#       self.to_chill()
#     elif live_cube == 4:
#       self.say_hello()
#     elif live_cube == 5:
#       self.to_work()
#     elif live_cube == 6:
#       self.find_girl()
#     self.statistics()
#     self.is_alive()

# univer = University('Step', 'Computer Science')
# human = Student('Anton')
# for day in range(10):
# 	if human.alive == False:
# 		break
# 	human.live(day)