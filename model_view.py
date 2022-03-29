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

class ModelView(QMainWindow):
    """Analysis Model View class (GUI)"""
    def __init__(self):
        """View initializer"""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Analysis Model')
        self.setFixedSize(600, 600)
        # Set the central widget and the main layout
        self.mainLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.mainLayout)

        #TODO: Grab variable names and number from setup file

        self._setSetupInput() #just ask for setup file path

        numberOfVariables = self._getNumberOfVariables()
        variableNames = self._getVariableNames()

        '''
        self._setVariables(variableNames)

        self._setParameters()

        self._setAnalysisButton()
        '''

    
    def _setSetupInput(self):
        """Set Setup UI"""
        # Create setup layout
        self.setupLayout = QVBoxLayout()
        self.setupLabel = QLabel("Setup file")
        font = QFont()
        font.setBold(True)
        self.setupLabel.setFont(font)
        self.setupLayout.addWidget(self.setupLabel)
        
        self.setup = SetupFileInput()
        self.setupLayout.addWidget(self.setup)

        self.mainLayout.addLayout(self.setupLayout)

    

    def _getNumberOfVariables(self): 
        #TODO modify for json file
        '''
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
    '''
        return 0

    def _getVariableNames(self):
        return 0 

class SetupFileInput(QWidget):
        setup_file_name = ""   #SetupFile name

        """Custom widget for json setup data"""
        def __init__(self):
            super().__init__()
            
            self.setupLayout = QGridLayout()
            self.setLayout(self.setupLayout)

            self.variableLabel = QLabel("JSON setup file Path: ")
            self.setupInput = QLineEdit()
            self.setupInput.setReadOnly(True)
            self.setupInputBtn = QPushButton("Get File")


            #self.csvInputBtn.clicked.connect(self.getFile)

            self.setupLayout.addWidget(self.variableLabel, 0, 0)
            self.setupLayout.addWidget(self.setupInput, 0, 1)
            self.setupLayout.addWidget(self.setupInputBtn, 0, 2)
            