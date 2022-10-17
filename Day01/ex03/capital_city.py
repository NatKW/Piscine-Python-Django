import sys

def state_capital():
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	if len(sys.argv) == 2:
		state = sys.argv[1]
		if state in states:
			symbols = states.get(state)
			print(capital_cities.get(symbols))
		else:
			print("unknown state")

if __name__ == '__main__':
	state_capital()


