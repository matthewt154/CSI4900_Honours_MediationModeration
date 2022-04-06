import json
import nibabel as nib 
import numpy as np
import pandas as pd

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


filepath = "Data/test_model.json"

with open(filepath, 'r') as f:
    data = json.load(f)

ModelName = data["ModelName"]
Direct = data["Direct"]
Interaction = data["Interaction"]
Path = data["Path"]
Variables = data["Variables"]
#Out = data["Out"]
#In = data["In"]
#Inter = data["Inter"]

#print(ModelName)
#print(Direct)
#print(Interaction)
#print(Path)
#print(Variables)

# Read variable data
for i,_ in enumerate(Variables):
    var_name = Variables[i]["variable_name"]
    var_type = Variables[i]["data_type"]
    
    if var_type == "csv":
        data_filepath = Variables[i]["filepath"]
        column = Variables[i]["column"]

        X = pd.read_csv(data_filepath)
        print(list(X[column]))

    elif var_type == "brain image data (maskless)":
        data_filepath = Variables[i]["filepath"]

        img_data = load_img_data(data_filepath)

        print(img_data)

    elif var_type == "brain image data (with mask)":
        data_filepath = Variables[i]["filepath"]
        mask_filepath = Variables[i]["mask_filepath"]

        img_data = load_img_data(data_filepath)

        mask_data = load_img_data(mask_filepath)
        mask_data = create_mask(mask_data)

        brain_data = create_brain_data(img_data, mask_data)

        print(brain_data)