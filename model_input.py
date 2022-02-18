'''
	*Mediation and Moderation analysis of cognitive reserve 
	*Input processing file 
	*Created Feb 2022 
	* Authors: 
	-Matthew Tran 300028206
	-Alexandre Latimer 

'''
import nibabel as nb 

'''
Deliverable 1
Matt: Input generic setup file
Alex Data to be used (CSV stuff)
Parameters - Matt (first 2) Alex (last 2)
''' 

#function to check the setup file for the number of variables used  
def check_setup(setup_name):
	num_var=0
	#some code to check the file and count variables ...
	return num_var

def confidence_interval_menu (bootstrap_num):
	#code to output a menu to select confidence intervals for a certain bootstrap number 

setup_name = input ("Please enter the name of the Model Setup File (make sure it's in the same directory")
model_variables = check_setup(setup_name)


#User parameters 
bootstrap_num = input("How many bootstraps (default 1000) do you want to include?")

confidence_interval_menu(bootstrap_num)

TFCE = input ("Do you want to apply TFCE (Y/N)")



