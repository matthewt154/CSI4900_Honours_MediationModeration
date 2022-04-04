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

class BrainImageInput(QWidget):
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
    
    def isIncomplete(self):
        '''Returns True if the input is incomplete'''     
        return not bool(self.brainImageInput.text())