import operator

#----------------------------------------ANIMAL----------------------------------------

class animal(object) :
	def __init__(self, name) :
		self.name = name
		self.eyes = 2
		self.eyecolour = "black"
		print("-----------------------------------------------------------------")
	def getLegs(self) :
		return self.legs
	def getEyes(self) :
		return self.eyes
	def getEars(self) :
		return self.ears
	def getEyecolour(self) :
		return self.eyecolour
	def setEyecolour(self, colour) :
		self.eyecolour = colour
	def digest(self) :
		pass
	def eat(self, food) :
		print(self.name + " ate the " + food)
		self.digest()

#-----------------------------------------------------MAMMAL---------------------------------

class mammal(animal) :
	def __init__(self, name) :
		self.legs = 4
		self.ears = 2
		self.nose = 1
		self.furcolour = "brown"
		animal.__init__(self, name)
		print(self.name + " is a mammal.")
	def getNose(self) :
		return self.nose
	def getFurcolour(self) :
		return self.furcolour
	def setFurcolour(self, colour) :
		self.furcolour = colour

#----------------------------------------------------BIRD----------------------------------

class bird(animal) :
	def __init__(self, name) :
		self.legs = 2
		self.beak = 1
		self.feathercolour = "black"
		animal.__init__(self, name)
		print(self.name + " is a bird.")
	def getBeak(self) :
		return self.beak
	def getFeathercolour(self) :
		return self.feathercolour
	def setFeathercolour(self, colour) :
		self.feathercolour = colour

#-----------------------------------REPTILE------------------------------------

class reptile(animal) :
	def __init__(self, name) :
		self.legs = 4
		self.nose = 1
		self.scalecolour = "green"
		animal.__init__(self, name)
		print(self.name + " is a reptile.")
	def getNose(self) :
		return self.nose
	def getScalecolour(self) :
		return self.scalecolour
	def setScalecolour(self, colour) :
		self.scalecolour = colour


#--------------------------------------CAT-----------------------------------
class cat(mammal) :
	def __init__(self, name) :
		mammal.__init__(self, name)
	def speak(self) :
		print("Meow")
	

	def main(self) :
		print(self.name + " is a cat with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("yellow")
		self.setFurcolour("white")
		print(self.name + " is a cat with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("mouse")
		

#---------------------------------------------COW--------------------------------
class cow(mammal) :
	def __init__(self, name) :
		mammal.__init__(self, name)
	def speak(self) :
		print("Moo")
	

	def main(self) :
		print(self.name + " is a cow with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFurcolour("brown")
		print(self.name + " is a cow with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("grass")
		

#---------------------------------------CROCODILE-------------------------------------
class crocodile(reptile) :
	def __init__(self, name) :
		reptile.__init__(self, name)
	def speak(self) :
		print("Grunt")
	

	def main(self) :
		print(self.name + " is a crocodile with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("black")
		self.setScalecolour("brown")
		print(self.name + " is a crocodile with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("fish")
		
#------------------------------------------CROW---------------------------------------
class crow(bird) :
	def __init__(self, name) :
		bird.__init__(self, name)
	def speak(self) :
		print("Caw")
	
	def main(self) :
		print(self.name + " is a crow with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFeathercolour("black")
		print(self.name + " is a crow with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("rat")
		

#---------------------------------------------DOG------------------------------------
class dog(mammal) :
	def __init__(self, name) :
		mammal.__init__(self, name)
	def speak(self) :
		print("Woof")
	

	def main(self) :
		print(self.name + " is a dog with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFurcolour("golden")
		print(self.name + " is a dog with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("chicken")
		

#--------------------------------------DUCK--------------------------------------------
class duck(bird) :
	def __init__(self, name) :
		bird.__init__(self, name)
	def speak(self) :
		print("Quack")
	

	def main(self) :
		print(self.name + " is a duck with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("red")
		self.setFeathercolour("brown")
		print(self.name + " is a duck with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("corn")
		

#-----------------------------------------------HORSE---------------------------------
class horse(mammal) :
	def __init__(self, name) :
		mammal.__init__(self, name)
	def speak(self) :
		print("Neigh")
	
	def main(self) :
		print(self.name + " is a horse with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFurcolour("white")
		print(self.name + " is a horse with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("apple")
		

#-------------------------------------------LION-----------------------------------
class lion(mammal) :
	def __init__(self, name) :
		mammal.__init__(self, name)
	def speak(self) :
		print("Roar")
	

	def main(self) :
		print(self.name + " is a lion with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("yellow")
		print(self.name + " is a lion with " + self.getFurcolour() + " fur and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("meat")
		

#--------------------------------------------PARROT--------------------------------
class parrot(bird) :
	def __init__(self, name) :
		bird.__init__(self, name)
	def speak(self) :
		print("Squawk")
	

	def main(self) :
		print(self.name + " is a parrot with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setFeathercolour("red")
		print(self.name + " is a parrot with " + self.getFeathercolour() + " feathers and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("chilli")
	
#------------------------------------------SNAKE--------------------------------------------
class snake(reptile) :
	def __init__(self, name) :
		reptile.__init__(self, name)
	def speak(self) :
		print("Hiss")
	

	def main(self) :
		print(self.name + " is a snake with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("yellow")
		self.setScalecolour("green")
		self.setScalecolour("yellow")
		print(self.name + " is a snake with " + self.getScalecolour() + " scales and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("mouse")
		

#-----------------------------------------------------------------------------------------------

if __name__ == "__main__" :
	a1 = cat("Tom")
	a1.main()

	a2 = cow("Tauros")
	a2.main()

	a3 = crocodile("Krok")
	a3.main()

	a4 = crow("Fandry")
	a4.main()

	a5 = dog("Jimmy")
	a5.main()

	a6 = duck("Donald")
	a6.main()

	a7 = horse("Rapidash")
	a7.main()

	a8 = lion("Leo")
	a8.main()

	a9 = parrot("Fearow")
	a9.main()

	a10 = snake("Seviper")
	a10.main()