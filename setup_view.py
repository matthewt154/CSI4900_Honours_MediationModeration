import string
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

import os
import main

class SetupView(QMainWindow):
    """Analysis Setup View class (GUI)"""
    def __init__(self):
        """View initializer"""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Analysis Setup')
        self.setFixedSize(1000, 1000)
        # Set the central widget and the main layout
        self.mainLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.mainLayout)

        self.mainlink = main.ModelSelect()
        #TODO: Link up to Model's variables + functionality
        self.variableNames = self.mainlink.getModelVariables() #["A", "B", "C", "D"]
        
        print("Variable names: "+str(self.variableNames))
        self._setVariables(self.variableNames)

        self._setParameters()

        self._setAnalysisButton()

    def _setVariables(self, variableNameList):
        """Set Variables UI"""
        # Create variables layout
        self.variablesLayout = QVBoxLayout()
        self.variablesLabel = QLabel("Variables")
        font = QFont()
        font.setBold(True)
        self.variablesLabel.setFont(font)
        self.variablesLayout.addWidget(self.variablesLabel)

        # Create variable inputs for each variable
        self.variables = {}
        for var in variableNameList:
            self.variables[var] = VariableInput(var)
            self.variablesLayout.addWidget(self.variables[var])

        self.mainLayout.addLayout(self.variablesLayout)

    def _setParameters(self):
        """Set Paramaters UI"""
        # Create parameters layout
        self.paramatersLayout = QVBoxLayout()
        self.paramatersLabel = QLabel("Paramaters")
        font = QFont()
        font.setBold(True)
        self.paramatersLabel.setFont(font)
        self.paramatersLayout.addWidget(self.paramatersLabel)

        # Number of Bootstraps
        self.bootstrapsLayout = QHBoxLayout()
        self.bootstrapsLabel = QLabel("Number of Bootstraps: ")
        self.bootstraps = QLineEdit("1000")
        self.bootstraps.setValidator(QIntValidator())
        self.bootstrapsLayout.addWidget(self.bootstrapsLabel)
        self.bootstrapsLayout.addWidget(self.bootstraps)
        self.paramatersLayout.addLayout(self.bootstrapsLayout)

        # Confidence Interval
        self.confidenceIntervalLayout = QHBoxLayout()
        self.confidenceIntervalLabel = QLabel("Confidence Interval: ")
        self.confidenceInterval = QComboBox()
        self.confidenceInterval.addItems(["Percentile", "Bias-Corrected"])
        self.confidenceIntervalLayout.addWidget(self.confidenceIntervalLabel)
        self.confidenceIntervalLayout.addWidget(self.confidenceInterval)
        self.paramatersLayout.addLayout(self.confidenceIntervalLayout)

        # TCFE
        self.tcfeLayout = QHBoxLayout()
        self.tcfeLabel = QLabel("TCFE: ")
        self.tcfe = QComboBox()
        self.tcfe.addItems(["No", "Yes"])
        self.tcfeLayout.addWidget(self.tcfeLabel)
        self.tcfeLayout.addWidget(self.tcfe)
        self.paramatersLayout.addLayout(self.tcfeLayout)

        # Multiple Comparision Correction 
        self.comparisonsLayout = QHBoxLayout()
        self.comparisonsLabel = QLabel("Correction for multiple comparisons: ")
        self.comparisons = QComboBox()
        self.comparisons.addItems(["None", "Family-wise", "False-discovery"])
        self.comparisonsLayout.addWidget(self.comparisonsLabel)
        self.comparisonsLayout.addWidget(self.comparisons)
        self.paramatersLayout.addLayout(self.comparisonsLayout)

        # Add parameters to main Layout
        self.mainLayout.addLayout(self.paramatersLayout)

    def _setAnalysisButton(self):
        """Set Analysis Button"""
        self.analysisBtn = QPushButton("Create Analysis File")
        self.mainLayout.addWidget(self.analysisBtn)
    
    def setModelVariables(self, data: dict):
        self.variableNames = data["name_variables"]


class CsvInput(QWidget):
    """Custom widget for csv data"""
    def __init__(self):
        super().__init__()
        
        self.csvLayout = QGridLayout()
        self.setLayout(self.csvLayout)

        self.variableLabel = QLabel("Csv File Path: ")
        self.csvInput = QLineEdit()
        self.csvInput.setReadOnly(True)
        self.csvInputBtn = QPushButton("Get File")
        self.columnLabel = QLabel("Column: ")
        self.csvInputColumn = QComboBox()


        #self.csvInputBtn.clicked.connect(self.getFile)

        self.csvLayout.addWidget(self.variableLabel, 0, 0)
        self.csvLayout.addWidget(self.csvInput, 0, 1)
        self.csvLayout.addWidget(self.csvInputBtn, 0, 2)
        self.csvLayout.addWidget(self.columnLabel, 1, 0)
        self.csvLayout.addWidget(self.csvInputColumn, 1, 1)

class BrainImageInput(QWidget):
    """Custom widget for maskless brain image data"""
    def __init__(self):
        super().__init__()
        
        self.brainImageLayout = QGridLayout()
        self.setLayout(self.brainImageLayout)

        self.variableLabel = QLabel("Brain Image File Path: ")
        self.brainImageInput = QLineEdit()
        self.brainImageInput.setReadOnly(True)
        self.brainImageInputBtn = QPushButton("Get File")


        #self.csvInputBtn.clicked.connect(self.getFile)

        self.brainImageLayout.addWidget(self.variableLabel, 0, 0)
        self.brainImageLayout.addWidget(self.brainImageInput, 0, 1)
        self.brainImageLayout.addWidget(self.brainImageInputBtn, 0, 2)

class BrainImageMaskInput(QWidget):
    """Custom widget for brain image data with mask"""
    def __init__(self):
        super().__init__()
        
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


        #self.csvInputBtn.clicked.connect(self.getFile)

        self.brainImageLayout.addWidget(self.variableLabel, 0, 0)
        self.brainImageLayout.addWidget(self.brainImageInput, 0, 1)
        self.brainImageLayout.addWidget(self.brainImageInputBtn, 0, 2)
        self.brainImageLayout.addWidget(self.maskLabel, 1, 0)
        self.brainImageLayout.addWidget(self.maskInput, 1, 1)
        self.brainImageLayout.addWidget(self.maskInputBtn, 1, 2)

class VariableInput(QWidget):

    variableName = ""   #Variable name

    def __init__(self, vname):
        super().__init__()

        variableName = vname

        self.variableInputLayout = QVBoxLayout()

        self.variablesLabel = QLabel("Variable " + variableName)
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
