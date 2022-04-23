from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QFont

import os
import json

class ModelView(QMainWindow):
    """Analysis Model View class (GUI)"""
    def __init__(self):
        """Initialize View"""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Analysis Model')
        self.setFixedSize(600, 400)
        # Set the central widget and the main layout
        self.mainLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.mainLayout)

        self._setSetupInput()

    
    def _setSetupInput(self):
        """Set the Setup UI"""
        # Create setup layout
        self.setupLayout = QVBoxLayout()
        self.setupLabel = QLabel("Setup file")
        font = QFont()
        font.setBold(True)
        self.setupLabel.setFont(font)
        self.setupLayout.addWidget(self.setupLabel)

        description1 = "Choose a json setup file and click submit. "
        description2 = "This will bring you to the variable selection page with the number of variables and their names already separated."        
        self.description1Label = QLabel(description1)
        self.setupLayout.addWidget(self.description1Label)
        self.description2Label = QLabel(description2)
        self.setupLayout.addWidget(self.description2Label)

        

        self.setup = SetupFileInput()
        self.setupLayout.addWidget(self.setup)

        self.mainLayout.addLayout(self.setupLayout)

        self.setup.variables_names = []
        self.setup.modelJson = {}

    def connectSubmitButton(self, lambda_fnc):
        """Connect the submit button with a lambda function"""
        self.setup.submitBtn.clicked.connect(lambda_fnc)

    def getVariables(self):
        """Get variable names"""
        return self.setup.variables_names
    
    def getModelJson(self):
        """Get modelJson from the input"""
        return self.setup.modelJson

class SetupFileInput(QWidget):
        """Custom widget for json setup data"""
        def __init__(self):
            super().__init__()
            
            self.setupLayout = QGridLayout()
            self.setLayout(self.setupLayout)

            self.variableLabel = QLabel("JSON setup file Path: ")
            self.setupInput = QLineEdit()
            self.setupInput.setReadOnly(True)
            self.outputLabel = QLabel("Setup output: ")
            self.setupOutput = QLineEdit()
            self.setupOutput.setReadOnly(True)

            self.setupInputBtn = QPushButton("Get File")

            self.submitBtn = QPushButton("Submit")

            #when button pushed get file using function
            self.setupInputBtn.clicked.connect(self.getFile)

            #pushing submit button to send data
            self.submitBtn.clicked.connect(self.submitNextPage)

            self.setupLayout.addWidget(self.variableLabel, 0, 0)
            self.setupLayout.addWidget(self.setupInput, 0, 1)
            self.setupLayout.addWidget(self.setupInputBtn, 0, 2)
            self.setupLayout.addWidget(self.outputLabel, 1, 0)
            self.setupLayout.addWidget(self.setupOutput, 1, 1)
            self.setupLayout.addWidget(self.submitBtn, 2, 1)

        '''Get Dialog Box to get filepath and update class'''
        def getFile(self):
            
            file_filter = 'Data File (*.json)'
            filepath,_ = QFileDialog.getOpenFileName(
                parent=self,
                caption='Select a data file',
                directory=os.getcwd(),
                filter=file_filter,
                initialFilter='Data File (*.json)'
            )
            #print(filepath)

            if filepath:
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                    print(str(list(data))) #all the json elements present

                    self.setupInput.setText(filepath)
                    
                    filepath=self.setupInput.text()
            
                    model_output = {
                        "number_variables":self._getNumberOfVariables(filepath),
                        "name_variables":self._getVariableNames(filepath),
                        "model_name":self._getModelName(filepath)
                    }

                    self.variables_names = self._getVariableNames(filepath)
                    self.modelJson = data

                    print(model_output)
                    self.setupOutput.setText(json.dumps(model_output))
                except FileNotFoundError as e:
                    print("File '%s' could not be found" % e.filename)
            return str(filepath)

        '''Variables to send over '''
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

        '''Submit button'''
        def submitNextPage(self):
            print("Submitted setup info succesfully")
            return 0
            