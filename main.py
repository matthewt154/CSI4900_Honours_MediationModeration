
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtWidgets

# import window views
import model_view
import setup_view

class Window(QtWidgets.QMainWindow):
    """Main Window"""

    def __init__(self, parent=None):
        """Initialise the main window"""
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
        self.model.connectSubmitButton(lambda: self.setup.setModelJson(self.model.getModelJson()))

        # Model page is first page
        self.goto("main")
        

    def register(self, widget, name):
        """Register a widget to the stacked_widget of the main window"""
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
    

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        """Switch main page view to given widget view"""
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
            


