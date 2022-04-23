from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog

import os
from functools import partial

class BrainImageMaskInput(QWidget):
    """Custom widget for brain image data with mask"""
    def __init__(self):
        """Initialize BrainImageMaskInput View"""
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
        """Get Dialog Box to get filepath and update QLineEdit input"""
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
        """Return data filepath string"""
        return str(self.brainImageInput.text())
    
    def getMaskFilepath(self):
        """Return mask filepath string"""
        return str(self.maskInput.text())
    
    def isIncomplete(self):
        """Returns True if the input is incomplete"""
        return not bool(self.brainImageInput.text()) or not bool(self.maskInput.text())