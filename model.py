
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
import model_view
#import model_input
import model_controller

def main():
    """Main function"""
    # Create an instance of QApplication
    model = QApplication(sys.argv)
    # Get and Show the view's GUI
    view = model_view.ModelView()
    view.show()
    #Get Model (?)
    #model = model_input.ModelInput()
    
    # Get controller
    model_controller.ModelController(view=view)
    # Execute the model gui main loop
    sys.exit(model.exec_())


if __name__ == '__main__':
    main()
