import random
from beverages import *

class CoffeeMachine:
	def __init__(self):
		self.served = 0

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90
			self.txt = "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			 super().__init__("This coffee machine has to be repaired.")

	def __init__(self) -> None:
		self.served = 0

	def repair(self):
		self.served = 0
		print("OK, the coffee machine has been fixed")
	
	def serve(self, beverage_choice: HotBeverage):
		if (self.served >= 10):
			raise CoffeeMachine.BrokenMachineException()
		self.served += 1
		if (random.randint(0, 1) == 1):
			return CoffeeMachine.EmptyCup()
		return beverage_choice ()

def test():
	machine = CoffeeMachine()
	for a in range(30):
		try:
			print(machine.serve(random.choice([Cappuccino, Coffee, Chocolate, Tea])))
		except CoffeeMachine.BrokenMachineException as e:
			print(e)
			machine.repair()

if __name__ == "__main__":
    test()