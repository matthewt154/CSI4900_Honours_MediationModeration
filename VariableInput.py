from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QStackedLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIntValidator, QFont

import numpy as np
import pandas as pd
import os
from functools import partial

from CsvInput import CsvInput
from BrainImageInput import BrainImageInput
from BrainImageMaskInput import BrainImageMaskInput

class VariableInput(QWidget):

    def __init__(self, vname):
        super().__init__()

        self.variableName = vname #Variable name

        self.variableInputLayout = QVBoxLayout()

        self.variablesLabel = QLabel("Variable " + self.variableName)
        self.variableInputLayout.addWidget(self.variablesLabel)


        self.variableNums = QComboBox()
        self.variableNums.addItems(["csv","brain image data (maskless)","brain image data (with mask)"])
        self.variableInputLayout.addWidget(self.variableNums)
        self.setLayout(self.variableInputLayout)

        self.variablesLayout = QStackedLayout()

        self.csv = CsvInput()
        self.brainImageData = BrainImageInput()
        self.brainImageMaskData = BrainImageMaskInput()

        self.variablesLayout.addWidget(self.csv)
        self.variablesLayout.addWidget(self.brainImageData)
        self.variablesLayout.addWidget(self.brainImageMaskData)

        self.variableInputLayout.addLayout(self.variablesLayout)

        self.variableNums.currentIndexChanged.connect(self.variablesLayout.setCurrentIndex)
    
    def getCurrentVariable(self):

        currentVar = self.variableNums.currentText()

        if currentVar == "csv":
            return {"variable_name": self.variableName,
                "data_type": "csv",
                "filepath": self.csv.getFilepath(),
                "column": self.csv.getColumn()}
        elif currentVar == "brain image data (maskless)":
            return {"variable_name": self.variableName,
                "data_type": "brain image data (maskless)",
                "filepath": self.brainImageData.getFilepath()}
        elif currentVar == "brain image data (with mask)":
            return {"variable_name": self.variableName,
                "data_type": "brain image data (with mask)",
                "filepath": self.brainImageMaskData.getFilepath(),
                "mask_filepath": self.brainImageMaskData.getMaskFilepath()}
    
    def isIncomplete(self):
        '''Returns True if the current input is incomplete'''
        currentVar = self.variableNums.currentText()

        if currentVar == "csv":
            return self.csv.isIncomplete()
        elif currentVar == "brain image data (maskless)":
            return self.brainImageData.isIncomplete()
        elif currentVar == "brain image data (with mask)":
            return self.brainImageMaskData.isIncomplete()
