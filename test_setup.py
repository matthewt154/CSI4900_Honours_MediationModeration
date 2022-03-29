import re
def check_setup(setup_name):
	f = open("Data/" +setup_name+".txt", "r")
	s = f.readline()
	print(s)
	content = s[s.find("[")+1:s.find("]")]
	print(content)
	
	num_var=0
	for c in content:
		if c.isalpha():
			num_var+=1
	return num_var

print (check_setup("setup_4"))