import json

def check_setup(setup_name):
	with open(setup_name, 'r') as f:
  		data = json.load(f)

	s = data["Direct"]
	
	return len(s[0])

print (check_setup("Data/model4_setup.json"))