
import sys

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
import json

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

# import view (GUI), model and controller
import model
import setup
import model_view
import setup_view
#import model_input
import model_controller

class PageWindow(QtWidgets.QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)


class ModelSelect(PageWindow):

    

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Model Selection")

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
        """Main Model selection function"""
        # Create an instance of QApplication
        #model = QApplication(sys.argv)
        # Get and Show the view's GUI
        """Analysis Model View class (GUI)"""
        # Set some main window's properties
        self.setWindowTitle('Analysis Model')
        self.setFixedSize(1000, 400)
        # Set the central widget and the main layout
        self.mainLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.mainLayout)


        self._setSetupInput() #just ask for setup file path

        # Execute the model gui main loop
        #sys.exit(model.exec_())
       

    def make_handleButton(self, button):
        def handleButton():
            if button == "modelSubmitButton": #transfer over to the variable selection page (setup)
                self.goto("setup")
        return handleButton
    
    def _setSetupInput(self):
        """Set Setup UI"""
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

        self.submitBtn = QtWidgets.QPushButton("Submit", self)
        self.submitBtn.clicked.connect(self.submitBtnClick("modelSubmitButton"))
        #print(self.setup.setupOutput.text())
        '''if (self.setup.setupOutput.text()):
            print("Something there")
            self.submitBtn.clicked.connect(self.submitBtnClick(self.setup.setupOutput.text()))'''
        
        self.setupLayout.addWidget(self.submitBtn)

        self.mainLayout.addLayout(self.setupLayout)
        
        '''self.submitBtn.clicked.connect(
            self.make_handleButton("modelSubmitButton"))'''
        
    def submitBtnClick(self, button):
        print("Submitted setup info succesfully")
        print(self.setup.setupOutput.text())
        def handleButton():
            if button == "modelSubmitButton": #transfer over to the variable selection page (setup)
                self.goto("setup")
        return handleButton
    
    @QtCore.pyqtSlot(str)
    def update_messages(self, message_a):
        self.message_a = message_a
        self.message_a_display.setText(self.message_a)


    def edit_messages(self):
        self.dialog = SetupWindow()
        self.dialog.set_messages(self.message_a)
        self.dialog.submitted.connect(self.update_messages)
        self.dialog.show()
    
    


class SetupWindow(PageWindow):
    submitted = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle("Variable selection")
        self.UiComponents()

    def goToMain(self):
        self.goto("main")

    def UiComponents(self):
        self.view = setup_view.SetupView()
        self.view.show()
        '''self.backButton = QtWidgets.QPushButton("BackButton", self)
        self.backButton.setGeometry(QtCore.QRect(5, 5, 100, 20))
        self.backButton.clicked.connect(self.goToMain)'''
    
    def set_messages(self, message_a):

        self.message_a_edit.setText(message_a)

    def on_submit(self):
        self.submitted.emit(
            self.message_a_edit.text()
            )
        self.close()


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        self.register(ModelSelect(), "main")
        self.register(SetupWindow(), "setup")

        self.goto("main")
        

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)
    

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


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
            self.outputLabel = QLabel("Setup output: ")
            self.setupOutput = QLineEdit()

            self.setupInputBtn = QPushButton("Get File")

            #self.submitBtn = QPushButton("Submit")

            #when button pushed get file using function
            self.setupInputBtn.clicked.connect(self.getFile)

            #pushing submit button to send data
            #self.submitBtn.clicked.connect(self.submitNextPage)

            self.setupLayout.addWidget(self.variableLabel, 0, 0)
            self.setupLayout.addWidget(self.setupInput, 0, 1)
            self.setupLayout.addWidget(self.setupInputBtn, 0, 2)
            self.setupLayout.addWidget(self.outputLabel, 1, 0)
            self.setupLayout.addWidget(self.setupOutput, 1, 1)
            #self.setupLayout.addWidget(self.submitBtn, 2, 1)

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


            if filepath:
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                    #print(str(list(data))) #all the json elements present

                    self.setupInput.setText(filepath)
                    
                    filepath=self.setupInput.text()
            
                    model_output = {
                        "number_variables":self._getNumberOfVariables(filepath),
                        "name_variables":self._getVariableNames(filepath),
                        "model_name":self._getModelName(filepath)
                    }
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

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
            


