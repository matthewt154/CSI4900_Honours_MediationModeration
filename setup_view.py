from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtGui import QIntValidator, QFont

import os
import json

from VariableInput import VariableInput

class SetupView(QMainWindow):
    """Analysis Setup View class (GUI)"""
    def __init__(self):
        """Initialize View"""
        super().__init__()

        # Set some main window's properties
        self.setWindowTitle('Analysis Setup')
        self.setFixedSize(600, 900)

        # Set the central widget and the main layout
        self.mainLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.mainLayout)

        #Set View 
        self._setVariablesView()
        self._setParametersView()
        self._setAnalysisButtonView()

        #Initialise modelJson
        self.modelJson = {}

    def _setVariablesView(self):
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
        self.scrollLayout = QVBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(self.scrollLayout)

        # Create variables dict
        self.variables = {}

        self.mainLayout.addLayout(self.variablesLayout)

    def _setParametersView(self):
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

    def _setAnalysisButtonView(self):
        """Set Analysis Button UI"""
        self.analysisBtn = QPushButton("Create Analysis File")
        self.mainLayout.addWidget(self.analysisBtn)

        self.analysisBtn.clicked.connect(self.createAnalysisFile)

    def createAnalysisFile(self):
        """Create Analysis File using the user inputs"""

        # Checks if any variables are incomplete
        for var in self.variables:
            if self.variables[var].isIncomplete():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Variable " + var + " is incomplete.")
                msg.exec_()
                return

        # Save Dialog for where to save json
        analysisFilePath,_ = QFileDialog.getSaveFileName(
            parent=self,
            caption='Save Analysis File as',
            directory=os.getcwd(),
            filter="Json File (*.json)"
        )

        if analysisFilePath:
            # Set setup model selected
            analysis_dict = self.modelJson

            # Set Variables 
            var_array = []
            for var in self.variables:
                print(self.variables[var].getCurrentVariable())
                var_array.append(self.variables[var].getCurrentVariable())
            analysis_dict["Variables"] = var_array

            # Set Paramaters
            analysis_dict["Bootstrap"] = str(self.bootstraps.text())
            analysis_dict["Confidence_Interval"] = str(self.confidenceInterval.currentText())
            analysis_dict["TFCE"] = str(self.tcfe.currentText())
            analysis_dict["Correction_Type"] = str(self.comparisons.currentText())

            # Create Json and write to output file
            analysisString = json.dumps(analysis_dict, indent=4)
            jsonFile = open(analysisFilePath, "w")
            jsonFile.write(analysisString)
            jsonFile.close()

    def setVariables(self, vnameList: list):
        """Set Variables to create the Variable Inputs"""
        self.variables = {}
        for var in vnameList:
            self.variables[var] = VariableInput(var)
            self.scrollLayout.addWidget(self.variables[var])
            self.scroll.setWidget(self.scrollContent)
    
    def setModelJson(self, modelJson: dict):
        """Set ModelJson with given dict"""
        self.modelJson = modelJson
        print(self.modelJson)
