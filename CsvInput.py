from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog

import pandas as pd
import os
from functools import partial


class CsvInput(QWidget):
    """Custom widget for csv data"""
    def __init__(self):
        """Initialize CsvInput View"""
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
        """Get Dialog Box to get filepath and update class"""
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
        """Return data filepath string"""
        return str(self.csvInput.text())
    
    def getColumn(self):
        """Return selected data column string"""
        return str(self.csvInputColumn.currentText())

    def isIncomplete(self):        
        """Returns True if the input is incomplete"""
        return not bool(self.csvInput.text()) or not bool(self.csvInputColumn.currentText())