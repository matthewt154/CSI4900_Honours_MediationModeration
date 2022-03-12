def check_setup(setup_name):
	f = open("Data/" +setup_name+".txt", "r")
	l_read = f.readline()
	result = re.search('[;(.*)]', l_read) #isolate stuff inside [] first line 
	num_var= re.search("';(.)'", result) 
	#some code to check the file and count variables ...
	return num_var

print (check_setup("setup_4"))