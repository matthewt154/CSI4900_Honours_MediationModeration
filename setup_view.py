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

class SetupView(QMainWindow):
    """Analysis Setup View class (GUI)"""
    def __init__(self):
        """View initializer"""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Analysis Setup')
        self.setFixedSize(600, 1000)
        # Set the central widget and the main layout
        self.mainLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.mainLayout)

        # Temporary place holder of datafile picker
        #TODO
        self.variableNums = QComboBox()
        self.variableNums.addItems(["csv","brain image data (maskless)","brain image data (with mask)"])
        self.mainLayout.addWidget(self.variableNums)

        self._setVariables()

        self._setParameters()

        self._setAnalysisButton()

    def _setVariables(self):
        """Set Variables UI"""
        self.variablesLayout = QStackedLayout()
        self.first = csvInput()
        self.second = QPushButton("maskless")
        self.third = QPushButton("mask")
        self.variablesLayout.addWidget(self.first)
        self.variablesLayout.addWidget(self.second)
        self.variablesLayout.addWidget(self.third)

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


class csvInput(QWidget):
    """Custom widget for csv data"""
    def __init__(self):
        super().__init__()
        
        self.csvLayout = QGridLayout()
        self.setLayout(self.csvLayout)

        self.variableLabel = QLabel("Csv File Path: ")
        self.csvInput = QLineEdit()
        self.csvInput.setReadOnly(True)
        self.csvInputBtn = QPushButton("Get File")


        #self.csvInputBtn.clicked.connect(self.getFile)

        self.csvLayout.addWidget(self.variableLabel, 0, 0)
        self.csvLayout.addWidget(self.csvInput, 0, 1)
        self.csvLayout.addWidget(self.csvInputBtn, 0, 2)
