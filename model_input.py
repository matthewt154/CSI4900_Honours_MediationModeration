'''
	*Mediation and Moderation analysis of cognitive reserve 
	*Input processing file 
	*Created Feb 2022 
	* Authors: 
	-Matthew Tran 300028206
	-Alexandre Latimer 300027473

'''
from msilib.schema import Error
import nibabel as nb 
import pandas as pd
import numpy as np

'''
Deliverable 1
Matt: Input generic setup file
Alex Data to be used (CSV stuff)
Parameters - Matt (first 2) Alex (last 2)
''' 

#function to check the setup file for the number of variables used  
def check_setup(setup_name):
	num_var=3
	#some code to check the file and count variables ...
	return num_var

def confidence_interval_menu (bootstrap_num):
	#code to output a menu to select confidence intervals for a certain bootstrap number 
	return

setup_name = input ("Please enter the name of the Model Setup File (make sure it's in the same directory")
model_variables = check_setup(setup_name)

# Data selection
try:
	data_output = pd.DataFrame()
	data_directory = input("Enter data file with variables: ")
	X = pd.read_csv(data_directory)
except FileNotFoundError as e:
	print("File '%s' could not be found" % e.filename)
	exit()

for x in range(model_variables):
	try:
		var = input("Select column for variable " + str(x+1) + "\n" + str(list(X)) + ": ")
		data_output[str(x)] = X[var]
		break
	except KeyError as e:
		print("Variable '%s' given is not included in data" % var)
		exit()
data_output.to_csv('data_output.csv', index=False)

#User parameters 
bootstrap_num = input("How many bootstraps (default 1000) do you want to include?")

confidence_interval_menu(bootstrap_num)

TFCE = input ("Do you want to apply TFCE (Y/N)")



