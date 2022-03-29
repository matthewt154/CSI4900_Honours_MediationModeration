'''
	*Mediation and Moderation analysis of cognitive reserve 
	*Input processing file 
	*Created Feb 2022 
	* Authors: 
	-Matthew Tran 300028206
	-Alexandre Latimer 300027473

'''
import json
import nibabel as nib 
import numpy as np
from msilib.schema import Error
import pandas as pd
import re

'''
Deliverable 1
Matt: Input generic setup file
Alex Data to be used (CSV stuff)
Parameters - Matt (first 2) Alex (last 2)
''' 

#--------functions given to read data ----------------- 
def load_img_data(path):
    """ Returns NIfTI brain image as a 4-D numpy array.
    Keyword arguments:
    path -- the path of the NIfTI file    
    """
    nii_img = nib.load(path)
    return nii_img.get_fdata()

def create_mask(img_data):
    """Returns image data where the voxels values are 0 or 1 based on if they are nan or not.
    Keyword arguments:
    img_data -- Loaded brain imaging data
    """
    return np.where(np.isnan(img_data), 0, 1)

def create_brain_data(img_data, mask):
    """Returns n by m sized brain imaging data.
    Keyword arguments:
    img_data -- Loaded brain imaging data
    mask -- Loaded brain imaging data that represents a mask
    """
    # Check if the mask and img_data are the same size later
    brain_data = []
    for i in range(img_data.shape[3]):
        p = np.multiply(img_data[:,:,:,i], mask)
        pf = p.flatten()
        pfn = pf[np.logical_not(np.isnan(pf))]
        brain_data.append(pfn)
    return np.array(brain_data)

#------------------------------------

#function to check the setup file for the number of variables used  

'''
Graph LR;
A --> C;
A --> B --> C;

'''

#check number of variables in setup file
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

def confidence_interval_menu (bootstrap_num):
	print("What type of confidence intervals would you like to use?")
	
	confidence_interval_type = input("1.Percentile (PE) \n 2.Bias-Corrected (BC)")
	# Selection from a menu/list * Percentile, Bias-Corrected
	return confidence_interval_type

def correction_menu():
    '''Menu for what correction for multiple comparisons to use'''
    print("Correction for multiple comparisons to use:")
    correction_type = input("1 - None\n2 - Family-wise\n3 - False-discovery\n")
    return correction_type

def write_output(filename, param_name, content):
	f = open(filename, "a")
	f.write(param_name + ": "+content)
	f.close()

# ============== User inputs =====================

#write output to a file

###model_num = input ("What model number is this?")
###out_name = "parameters_model"+str(model_num)+".txt"
###final_out = open(out_name, "x") #create file

setup_name = input ("Please enter the name of the Model Setup File (make sure it's in the 'Data' directory): ")
model_variables = check_setup(setup_name)
###write_output(final_out, "No. variables", model_variables)

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
###write_output(final_out, "Bootstraps", bootstrap_num)

confidence_type= confidence_interval_menu(bootstrap_num)
###write_output(final_out, "Confidence interval type", confidence_type)

TFCE = input ("Do you want to apply TFCE (Y/N)")
###write_output(final_out, "TFCE", TFCE)

correction_type = correction_menu()

#--------------- Output Analysis to JSON file ---------------

analysis_dict = {}
analysis_dict["Bootstrap"] = bootstrap_num
analysis_dict["Confidence_Interval"] = confidence_type
analysis_dict["TFCE"] = TFCE
analysis_dict["Correction_Type"] = correction_type

analysisString = json.dumps(analysis_dict)
jsonFile = open("analysis_output.json", "w")
jsonFile.write(analysisString)
jsonFile.close()