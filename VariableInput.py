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


class CsvInput2(QWidget):
    """Custom widget for csv data"""
    def __init__(self):
        super().__init__()

        self.setFixedHeight(100)
        
        self.csvLayout = QGridLayout()
        self.setLayout(self.csvLayout)

        self.variableLabel = QLabel("Csv File Path: ")
        self.csvInput = QLineEdit()
        self.csvInput.setReadOnly(True)
        self.csvInputBtn = QPushButton("Get File")
        self.columnLabel = QLabel("Column: ")
        self.csvInputColumn = QComboBox()


        self.csvLayout.addWidget(self.variableLabel, 0, 0)
        self.csvLayout.addWidget(self.csvInput, 0, 1)
        self.csvLayout.addWidget(self.csvInputBtn, 0, 2)
        self.csvLayout.addWidget(self.columnLabel, 1, 0)
        self.csvLayout.addWidget(self.csvInputColumn, 1, 1)

        self.csvInputBtn.clicked.connect(self.getFile)

    def getFile(self):
        '''Get Dialog Box to get filepath and update class'''
        file_filter = 'Data File (*.csv)'
        filepath,_ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File (*.csv)'
        )
        print(filepath)

        if filepath:
            try:
                X = pd.read_csv(filepath)
                print(str(list(X)))

                self.csvInput.setText(filepath)
                self.csvInputColumn.clear()
                self.csvInputColumn.addItems(list(X))
            except FileNotFoundError as e:
                print("File '%s' could not be found" % e.filename)
    
    def getFilepath(self):
        '''Return data filepath string'''
        return str(self.csvInput.text())
    
    def getColumn(self):
        '''Return selected data column string'''
        return str(self.csvInputColumn.currentText())

class BrainImageInput2(QWidget):
    """Custom widget for maskless brain image data"""
    def __init__(self):
        super().__init__()
        
        self.setFixedHeight(100)
        
        self.brainImageLayout = QGridLayout()
        self.setLayout(self.brainImageLayout)

        self.variableLabel = QLabel("Brain Image File Path: ")
        self.brainImageInput = QLineEdit()
        self.brainImageInput.setReadOnly(True)
        self.brainImageInputBtn = QPushButton("Get File")

        self.brainImageLayout.addWidget(self.variableLabel, 0, 0)
        self.brainImageLayout.addWidget(self.brainImageInput, 0, 1)
        self.brainImageLayout.addWidget(self.brainImageInputBtn, 0, 2)

        self.brainImageInputBtn.clicked.connect(self.getFile)

    def getFile(self):
        '''Get Dialog Box to get filepath and update class'''
        file_filter = 'Nii File (*.nii.gz)'
        filepath,_ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Nii File (*.nii.gz)'
        )
        print(filepath)

        if filepath:
            try:
                self.brainImageInput.setText(filepath)
            except FileNotFoundError as e:
                print("File '%s' could not be found" % e.filename)
    
    def getFilepath(self):
        '''Return data filepath string'''
        return str(self.brainImageInput.text())

class BrainImageMaskInput2(QWidget):
    """Custom widget for brain image data with mask"""
    def __init__(self):
        super().__init__()

        self.setFixedHeight(100)
        
        self.brainImageLayout = QGridLayout()
        self.setLayout(self.brainImageLayout)

        self.variableLabel = QLabel("Brain Image File Path: ")
        self.brainImageInput = QLineEdit()
        self.brainImageInput.setReadOnly(True)
        self.brainImageInputBtn = QPushButton("Get File")
        self.maskLabel = QLabel("Mask File Path: ")
        self.maskInput = QLineEdit()
        self.maskInput.setReadOnly(True)
        self.maskInputBtn = QPushButton("Get File")

        self.brainImageLayout.addWidget(self.variableLabel, 0, 0)
        self.brainImageLayout.addWidget(self.brainImageInput, 0, 1)
        self.brainImageLayout.addWidget(self.brainImageInputBtn, 0, 2)
        self.brainImageLayout.addWidget(self.maskLabel, 1, 0)
        self.brainImageLayout.addWidget(self.maskInput, 1, 1)
        self.brainImageLayout.addWidget(self.maskInputBtn, 1, 2)

        self.brainImageInputBtn.clicked.connect(partial(self.getFile, self.brainImageInput))
        self.maskInputBtn.clicked.connect(partial(self.getFile, self.maskInput))

    def getFile(self, input: QLineEdit):
        '''Get Dialog Box to get filepath and update QLineEdit input'''
        file_filter = 'Nii File (*.nii.gz)'
        filepath,_ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Nii File (*.nii.gz)'
        )
        print(filepath)

        if filepath:
            try:
                input.setText(filepath)
            except FileNotFoundError as e:
                print("File '%s' could not be found" % e.filename)
    
    def getFilepath(self):
        '''Return data filepath string'''
        return str(self.brainImageInput.text())
    
    def getMaskFilepath(self):
        '''Return mask filepath string'''
        return str(self.maskInput.text())

