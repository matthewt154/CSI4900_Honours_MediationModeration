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
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtGui import QIntValidator, QFont

import os

import json

from VariableInput import VariableInput

#import main


class SetupView(QMainWindow):
    """Analysis Setup View class (GUI)"""
    def __init__(self):
        """View initializer"""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Analysis Setup')

        self.setFixedSize(600, 900)

        # Set the central widget and the main layout
        self.mainLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.mainLayout)

        #self.mainlink = main.ModelSelect()
        #TODO: Link up to Model's variables + functionality
        #self.variableNames = self.mainlink.getModelVariables() #["A", "B", "C", "D"]
        #self.variableNames = ["A", "B", "C", "D"]
        
        #print("Variable names: "+str(self.variableNames))
        #self._setVariables(self.variableNames)
        self.NEW_setVariables()

        self._setParameters()

        self._setAnalysisButton()

    def setVariables(self, vnameList):
        self.variables = {}
        for var in vnameList:
            self.variables[var] = VariableInput(var)
            self.variablesLayout.addWidget(self.variables[var])

    def NEW_setVariables(self):
        """Set Variables UI"""
        # Create variables layout
        self.variablesLayout = QVBoxLayout()
        self.variablesLabel = QLabel("Variables")
        font = QFont()
        font.setBold(True)
        self.variablesLabel.setFont(font)
        self.variablesLayout.addWidget(self.variablesLabel)

        # Create variables dict
        self.variables = {}

        self.mainLayout.addLayout(self.variablesLayout)

    def _setVariables(self, variableNameList):
        """Set Variables UI"""
        # Create variables layout
        self.variablesLayout = QVBoxLayout()
        self.variablesLabel = QLabel("Variables")
        font = QFont()
        font.setBold(True)
        self.variablesLabel.setFont(font)
        self.variablesLayout.addWidget(self.variablesLabel)

        # Add the Scrollable Area
        self.scroll = QScrollArea()
        self.variablesLayout.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scrollContent = QWidget(self.scroll)
        # Add set Layout to Scrollable Area
        scrollLayout = QVBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(scrollLayout)

        # Create variable inputs for each variable
        self.variables = {}
        for var in variableNameList:
            self.variables[var] = VariableInput(var)
            scrollLayout.addWidget(self.variables[var])
            self.scroll.setWidget(self.scrollContent)

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

        self.analysisBtn.clicked.connect(self.createAnalysisFile)

    def createAnalysisFile(self):
        analysis_dict = {}

        var_array = []
        for var in self.variables:
            print(self.variables[var].getCurrentVariable())
            var_array.append(self.variables[var].getCurrentVariable())

        analysis_dict["Variables"] = var_array
        analysis_dict["Bootstrap"] = str(self.bootstraps.text())
        analysis_dict["Confidence_Interval"] = str(self.confidenceInterval.currentText())
        analysis_dict["TFCE"] = str(self.tcfe.currentText())
        analysis_dict["Correction_Type"] = str(self.comparisons.currentText())

        analysisString = json.dumps(analysis_dict)
        jsonFile = open("analysis_output.json", "w")
        jsonFile.write(analysisString)
        jsonFile.close()

    
    def setModelVariables(self, data: dict):
        self.variableNames = data["name_variables"]
