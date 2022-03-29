
import json
import re
import nibabel as nib 
import numpy as np
from msilib.schema import Error
import pandas as pd

class ModelInput():
    """Analysis Model input class"""

    analysis_dict = {}  # Analysis file json dictionary

    def __init__(self):
        """Initialise default paramaters"""
        self.analysis_dict["Bootstraps"] = "1000"
        self.analysis_dict["Confidence_Interval"] = "Percentile"
        self.analysis_dict["TCFE"] = "No"
        self.analysis_dict["Correction_Type"] = "None"

    def _getNumberOfVariables(self, setup_name): 
        with open(setup_name, 'r') as f:
            data = json.load(f)

        s = data["Direct"]
        
        return len(s[0])

    def _getVariableNames(self, setup_name):
        with open(setup_name, 'r') as f:
            data = json.load(f)

        s = data["Direct"]
        
        return s[0]
    
    def _getModelName(self, setup_name):
        with open(setup_name, 'r') as f:
            data = json.load(f)
        return data["ModelName"]

    
    '''def _updateParamaters(self, key, value):
        self.analysis_dict[key] = value

    def _createAnalysisFile(self):
        """Saves Json analysis file"""
        analysisString = json.dumps(self.analysis_dict)
        jsonFile = open("analysis_output.json", "w")
        jsonFile.write(analysisString)
        jsonFile.close()
    '''
