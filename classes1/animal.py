import operator

#--------------------------------------CAT-----------------------------------
class cat() :
	def __init__(self, name) :
		self.__legs = 4 #private members
		self.__eyes = 2
		self.__ears = 2
		self.__nose = 1
		self.__eyecolour = "green"
		self.__furcolour = "brown"
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getEars(self) :
		return self.__ears
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFurcolour(self) :
		return self.__furcolour
	def setFurcolour(self, colour) :
		self.__furcolour = colour
	def speak(self) :
		print("Meow")
	def __digest(self) :
		pass
	def eat(self, food) :
		print(a1.__name + " ate the " + food)
		a1.__digest()

	def main(self) :
		print(a1.__name + " is a cat with " + a1.getFurcolour() + " fur and " + a1.getEyecolour() + " eyes.")
		a1.setEyecolour("yellow")
		a1.setFurcolour("white")
		print(a1.__name + " is a cat with " + a1.getFurcolour() + " fur and " + a1.getEyecolour() + " eyes.")
		a1.speak()
		a1.eat("mouse")
		

#---------------------------------------------COW--------------------------------
class cow() :
	def __init__(self, name) :
		self.__legs = 4
		self.__eyes = 2
		self.__ears = 2
		self.__nose = 1
		self.__eyecolour = "black"
		self.__coatcolour = "white"
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getEars(self) :
		return self.__ears
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getCoatcolour(self) :
		return self.__coatcolour
	def setCoatcolour(self, colour) :
		self.__coatcolour = colour
	def speak(self) :
		print("Moo")
	def __digest(self) :
                pass
	def eat(self, food) :
		print(self.__name + " ate the " + food)
		self.__digest()


	def main(self) :
		print(self.__name + " is a cow with " + self.getCoatcolour() + " coat and " + self.getEyecolour() + " eyes.")
		self.setEyecolour("brown")
		self.setCoatcolour("brown")
		print(self.__name + " is a cow with " + self.getCoatcolour() + " coat and " + self.getEyecolour() + " eyes.")
		self.speak()
		self.eat("grass")
		

#---------------------------------------CROCODILE-------------------------------------
class crocodile() :
	def __init__(self, name) :
		self.__legs = 4
		self.__eyes = 2
		self.__nose = 1
		self.__eyecolour = "yellow"
		self.__scalecolour = "green"
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getScalecolour(self) :
		return self.__scalecolour
	def speak(self) :
		print("Grunt")
	def __digest(self) :
		pass
	def eat(self, food) :
		print(a3.__name + " ate the " + food)
		a3.__digest()

	def main(self) :
		print(a3.__name + " is a crocodile with " + a3.getScalecolour() + " scales and " + a3.getEyecolour() + " eyes.")
		a3.setEyecolour("black")
		print(a3.__name + " is a crocodile with " + a3.getScalecolour() + " scales and " + a3.getEyecolour() + " eyes.")
		a3.speak()
		a3.eat("fish")
		

#------------------------------------------CROW---------------------------------------
class crow() :
	def __init__(self, name) :
		self.__legs = 2
		self.__eyes = 2
		self.__beak = 1
		self.__eyecolour = "black"
		self.__feathercolour = "black"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getBeak(self) :
		return self.__beak
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFeathercolour(self) :
		return self.__feathercolour
	def setFeathercolour(self, colour) :
		self.__feathercolour = colour
	def speak(self) :
		print("Caw")
	def __digest(self) :
                pass
	def eat(self, food) :
		print(a4.__name + " ate the " + food)
		a4.__digest()

	def main(self) :
		print(a4.__name + " is a crow with " + a4.getFeathercolour() + " feathers and " + a4.getEyecolour() + " eyes.")
		a4.setEyecolour("brown")
		a4.setFeathercolour("black")
		print(a4.__name + " is a crow with " + a4.getFeathercolour() + " feathers and " + a4.getEyecolour() + " eyes.")
		a4.speak()
		a4.eat("rat")
		

#---------------------------------------------DOG------------------------------------
class dog() :
	def __init__(self, name) :
		self.__legs = 4
		self.__eyes = 2
		self.__ears = 2
		self.__nose = 1
		self.__eyecolour = "black"
		self.__furcolour = "brown"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getEars(self) :
		return self.__ears
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFurcolour(self) :
		return self.__furcolour
	def setFurcolour(self, colour) :
		self.__furcolour = colour
	def speak(self) :
		print("Woof")
	def __digest(self) :
                pass
	def eat(self, food) :
		print(a5.__name + " ate the " + food)
		a5.__digest()

	def main(self) :
		print(a5.__name + " is a dog with " + a5.getFurcolour() + " fur and " + a5.getEyecolour() + " eyes.")
		a5.setEyecolour("brown")
		a5.setFurcolour("golden")
		print(a5.__name + " is a dog with " + a5.getFurcolour() + " fur and " + a5.getEyecolour() + " eyes.")
		a5.speak()
		a5.eat("chicken")
		

#--------------------------------------DUCK--------------------------------------------
class duck() :
	def __init__(self, name) :
		self.__legs = 2
		self.__eyes = 2
		self.__beak = 1
		self.__eyecolour = "black"
		self.__feathercolour = "white"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getBeak(self) :
		return self.__beak
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFeathercolour(self) :
		return self.__feathercolour
	def setFeathercolour(self, colour) :
		self.__feathercolour = colour
	def speak(self) :
		print("Quack")
	def __digest(self) :
                pass
	def eat(self, food) :
		print(a6.__name + " ate the " + food)
		a6.__digest()

	def main(self) :
		print(a6.__name + " is a duck with " + a6.getFeathercolour() + " feathers and " + a6.getEyecolour() + " eyes.")
		a6.setEyecolour("red")
		a6.setFeathercolour("brown")
		print(a6.__name + " is a duck with " + a6.getFeathercolour() + " feathers and " + a6.getEyecolour() + " eyes.")
		a6.speak()
		a6.eat("corn")
		

#-----------------------------------------------HORSE---------------------------------
class horse() :
	def __init__(self, name) :
		self.__legs = 4
		self.__eyes = 2
		self.__ears = 2
		self.__nose = 1
		self.__eyecolour = "black"
		self.__furcolour = "brown"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getEars(self) :
		return self.__ears
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFurcolour(self) :
		return self.__furcolour
	def setFurcolour(self, colour) :
		self.__furcolour = colour
	def speak(self) :
		print("Neigh")
	def __digest(self) :
		pass
	def eat(self, food) :
		print(a7.__name + " ate the " + food)
		a7.__digest()

	def main(self) :
		print(a7.__name + " is a horse with " + a7.getFurcolour() + " fur and " + a7.getEyecolour() + " eyes.")
		a7.setEyecolour("brown")
		a7.setFurcolour("white")
		print(a7.__name + " is a horse with " + a7.getFurcolour() + " fur and " + a7.getEyecolour() + " eyes.")
		a7.speak()
		a7.eat("apple")
	

#-------------------------------------------LION-----------------------------------
class lion() :
	def __init__(self, name) :
		self.__legs = 4
		self.__eyes = 2
		self.__ears = 2
		self.__nose = 1
		self.__eyecolour = "green"
		self.__furcolour = "golden"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getEars(self) :
		return self.__ears
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFurcolour(self) :
		return self.__furcolour
	def speak(self) :
		print("Roar")
	def __digest(self) :
                pass
	def eat(self, food) :
		print(a8.__name + " ate the " + food)
		a8.__digest()

	def main(self) :
		print(a8.__name + " is a lion with " + a8.getFurcolour() + " fur and " + a8.getEyecolour() + " eyes.")
		a8.setEyecolour("yellow")
		print(a8.__name + " is a lion with " + a8.getFurcolour() + " fur and " + a8.getEyecolour() + " eyes.")
		a8.speak()
		a8.eat("meat")
		

#--------------------------------------------PARROT--------------------------------
class parrot() :
	def __init__(self, name) :
		self.__legs = 2
		self.__eyes = 2
		self.__beak = 1
		self.__eyecolour = "black"
		self.__feathercolour = "green"
		self.__position = (0, 0)
		self.__name = name
	def getLegs(self) :
		return self.__legs
	def getEyes(self) :
		return self.__eyes
	def getBeak(self) :
		return self.__beak
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getFeathercolour(self) :
		return self.__feathercolour
	def setFeathercolour(self, colour) :
		self.__feathercolour = colour
	def speak(self) :
		print("Squawk")
	def __digest(self) :
                pass
	def eat(self, food) :
		print(a9.__name + " ate the " + food)
		a9.__digest()

	def main(self) :
		print(a9.__name + " is a parrot with " + a9.getFeathercolour() + " feathers and " + a9.getEyecolour() + " eyes.")
		a9.setEyecolour("brown")
		a9.setFeathercolour("red")
		print(a9.__name + " is a parrot with " + a9.getFeathercolour() + " feathers and " + a9.getEyecolour() + " eyes.")
		a9.speak()
		a9.eat("chilli")
	
#------------------------------------------SNAKE--------------------------------------------
class snake() :
	def __init__(self, name) :
		self.__eyes = 2
		self.__nose = 1
		self.__eyecolour = "green"
		self.__scalecolour = "brown"
		self.__position = (0, 0)
		self.__name = name
	def getEyes(self) :
		return self.__eyes
	def getNose(self) :
		return self.__nose
	def getEyecolour(self) :
		return self.__eyecolour
	def setEyecolour(self, colour) :
		self.__eyecolour = colour
	def getScalecolour(self) :
		return self.__scalecolour
	def setScalecolour(self, colour) :
		self.__scalecolour = colour
	def speak(self) :
		print("Hiss")
	def __digest(self) :
		pass
	def eat(self, food) :
		print(a10.__name + " ate the " + food)
		a10.__digest()

	def main(self) :
		print(a10.__name + " is a snake with " + a10.getScalecolour() + " scales and " + a10.getEyecolour() + " eyes.")
		a10.setEyecolour("yellow")
		a10.setScalecolour("green")
		print(a10.__name + " is a snake with " + a10.getScalecolour() + " scales and " + a10.getEyecolour() + " eyes.")
		a10.speak()
		a10.eat("mouse")


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