
from beverages import HotBeverage

class CoffeeMachine:

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90
			self.txt = "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			 super().__init__("This coffee machine has to be repaired.")

	def repair():
		random.seed(2) 
		print("The Machine is fixed")
	
	def serve(HotBeverage):
		bevserved = random.choices(['Coffee', 'Tea', 'Chocolate', 'Capuccino' 'EmptyCup'], weights = [10, 1, 1], k = 10)




if __name__ == "__main__":
    test()