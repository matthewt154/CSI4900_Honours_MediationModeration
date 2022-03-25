
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel

# import view (GUI), model and controller
import setup_view
import setup_model
import setup_controller

def main():
    """Main function"""
    # Create an instance of QApplication
    setup = QApplication(sys.argv)
    # Get and Show the view's GUI
    view = setup_view.SetupView()
    view.show()
    # Get Model
    model = setup_model.SetupModel()
    # Get controller
    setup_controller.SetupController(model=model, view=view)
    # Execute the setup gui main loop
    sys.exit(setup.exec_())


if __name__ == '__main__':
    main()
