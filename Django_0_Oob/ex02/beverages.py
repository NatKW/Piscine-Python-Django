class HotBeverage:

	def __init__(self):
		self.name = 'hot beverage'
		self.price = 0.30
		self.txt = "Just some hot water in a cup."

	def description(self):
		return self.txt
	
	def __str__(self) -> str:
		text = ("name : {name}\n"
			"price: {price:0.2f}\n"
			"description: {description}")
		return(text.format(name=self.name, price=self.price, description=self.description()))

class Coffee(HotBeverage):
	def __init__(self):
		self.name = "coffee"
		self.price = 0.40
		self.txt = "A coffee, to stay awake."

class Tea(HotBeverage):
	def __init__(self):
		self.name = "tea"
		self.price = 0.30
		self.txt = "Just some hot water in a cup."

class Chocolate(HotBeverage):
	def __init__(self):
		self.name = "chocolate"
		self.price = 0.50
		self.txt = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self):
		self.name = "cappuccino"
		self.price = 0.45
		self.txt = "Un po' di Italia nella sua tazza!"

def test():

	print(HotBeverage())
	print(Coffee())
	print(Tea())	
	print(Chocolate())
	print(Cappuccino())

if __name__ == "__main__":
    test()
