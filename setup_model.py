
import json
import nibabel as nib 
import numpy as np
from msilib.schema import Error
import pandas as pd

class SetupModel():
    """Analysis Setup Model class"""

    analysis_dict = {}  # Analysis file json dictionary

    def __init__(self):
        """Initialise default paramaters"""
        self.analysis_dict["Bootstraps"] = "1000"
        self.analysis_dict["Confidence_Interval"] = "Percentile"
        self.analysis_dict["TCFE"] = "No"
        self.analysis_dict["Correction_Type"] = "None"

    def _updateParamaters(self, key, value):
        self.analysis_dict[key] = value

    def _createAnalysisFile(self):
        """Saves Json analysis file"""
        analysisString = json.dumps(self.analysis_dict)
        jsonFile = open("analysis_output.json", "w")
        jsonFile.write(analysisString)
        jsonFile.close()
    
