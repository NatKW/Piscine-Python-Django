import sys

def get_key_from_value(dict: dict, target: str):
	for key, item in dict.items():
		if item.lower() == target.lower():
			return key
	return None

def get_value_from_key(dict: dict, target: str):
	for key, item in dict.items():
		if key.lower() == target.lower():
			return item
	return None


def all_in(str: str):
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

	value = get_value_from_key(states, str)
	key = get_key_from_value(capital_cities, str)
	if key:
		print(capital_cities.get(key), "is the state capital of", get_key_from_value(states, key))
	elif value:
		print(get_key_from_value(states, value), "is the state of", capital_cities.get(value))
	else:
		print(str, "is neither a capital or a state")

def main():
	if len(sys.argv) != 2:
		return None
	elts = sys.argv[1].split(",")
	for elt in elts:
		elt = elt.strip()
		if elt == "":
			continue
		all_in(elt)

if __name__ == '__main__':
	main()
