from random import *
class Student:
	def __init__(self, name):
		self.name = name
		self.gladness = 50
		self.progress = 0
		self.strength = 5
		self.fatigue = 0
		self.money = 0
		self.alive = True
	def say_hello(self):
		print('Hello!')
	def to_study(self):
		print('Time to study!')
		self.progress += 5
		self.gladness -= 10
		self.fatigue += 10
	def to_sleep(self):
		print('Sleep time!')
		self.gladness += 5
		self.fatigue -= 10
	def to_chill(self):
		print('Chill time!')
		self.gladness += 15
		self.progress -= 5
		self.fatigue -= 5
		self.money -= -5
	def to_training(self):
		print('Gym time!')
		self.gladness += 5
		self.strength += 15
		self.progress -= 2
		self.fatigue += 15
		self.money -= 10
	def to_job(self):
		print('Work time!')
		self.gladness -= 10
		self.progress += 5
		self.fatigue += 20
		self.money += 10
	def is_alive(self):
		if self.progress < -40:
			print('When was the last time you were at school?')
			self.alive = False
		elif self.gladness < 15:
			print('Apathy and depression..')
			self.alive = False
		elif self.progress > 100:
			print('Too good, to be true!')
			self.alive = False
		elif self.strength > 45:
			print('Are you really human?!')
			self.alive = False
		elif self.fatigue < -70:
			print('Do you know what a sleeping is?')
			self.alive = False
		elif self.money > 50:
			print('Employee of the Year!')
			self.alive = False
	def statistics(self):
		print('Gladness = ', self.gladness, ' Progress = ', self.progress, 'Strength = ', self.strength, 'Fatigue = ', self.fatigue,)
	def live(self, day):
		day = 'Day ' + str(day) + ' of ' + self.name + ' life'
		print(day)
		live_cube = randint(1,4)
		if live_cube == 1:
			self.to_study()
		elif live_cube == 2:
			self.to_sleep()
		elif live_cube == 3:
			self.to_chill()
		elif live_cube == 4:
			self.say_hello()
		elif live_cube == 5:
			self.to_training()
		elif live_cube == 6:
			self.to_job()
		self.statistics()
		self.is_alive()




from random import *
class Dog:
	def __init__(self, name):
		self.name = name
    self.gladness = 10
		self.stamina = 5
		self.fatigue = 0
    self.hunger = 35
		self.alive = True
	def to_bark(self):
		print('Woof! Woof!')
	def to_walk(self):
		print('Time to go for a walk!')
		self.stamina += 5
		self.gladness += 10
		self.fatigue += 10
		self.hunger -= 10
	def to_sleep(self):
		print('Sleep time!')
		self.gladness += 5
		self.fatigue -= 10
    self.hunger -= 5
		self.stamina -= 5
	def to_chill(self):
		print('Stay at home and play with human!')
		self.gladness += 15
		self.fatigue -= 5
		self.hunger -= 10
		self.stamina += 1
	def to_eat(self):
		print('Lunch ready!')
		self.gladness += 10
		self.fatigue -= 5
		self.hunger += 25
		self.stamina -= 3
	def is_alive(self):
			self.alive = False
		elif self.gladness > 50:
			print('What?')
			self.alive = False
		elif self.fatigue > 25:
			print('You need a break')
			self.alive = False
		elif self.hunger > -30:
			print('Starvation..')
			self.alive = False
		elif self.stamina > -10:
			print('Your heart couldn`t take it')
	def statistics(self):
		print('Gladness = ', self.gladness, ' Fatigue = ', self.fatigue, 'Hunger = ', self.hunger, 'Stamina = ', self.stamina,)
	def live(self, day):
		day = 'Day ' + str(day) + ' of ' + self.name + ' life'
		print(day)
		live_cube = randint(1,4)
		if live_cube == 1:
			self.to_walk()
		elif live_cube == 2:
			self.to_sleep()
		elif live_cube == 3:
			self.to_chill()
		elif live_cube == 4:
			self.to_eat()
		elif live_cube == 5:
			self.to_bark()
		self.statistics()
		self.is_alive()

pet = Dog('Bruno')
for day in range(51):
	if pet.alive == False:
		break
	pet.live(day)




print("Hello World! And hello to my teacher")