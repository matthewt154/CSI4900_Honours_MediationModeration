
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

import setup_view
import model_view

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Create and register pages
        self.m_pages = {}
        self.model = model_view.ModelView()
        self.setup = setup_view.SetupView()

        self.register(self.model, "main")
        self.register(self.setup, "setup")

        # Connect Model's Submit Button to nextPage and setting Variables for setup page
        self.model.connectSubmitButton(lambda: self.goto("setup"))
        self.model.connectSubmitButton(lambda: self.setup.setVariables(self.model.getVariables()))

        # Model page is first page
        self.goto("main")
        

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
    

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())

def main():
    """Main function"""
    # Create an instance of QApplication and show
    setup = QApplication(sys.argv)
    main_page = Window()
    main_page.show()
    sys.exit(setup.exec_())

if __name__ == "__main__":
    main()
            


