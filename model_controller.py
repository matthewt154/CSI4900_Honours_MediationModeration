from functools import partial

from PyQt5.QtWidgets import QFileDialog
import os

import model_view

# Create a Controller class to connect the GUI and the model
class ModelController:
    """Analysis Model Controller class"""
    def __init__(self, view: model_view.ModelView):
        """Controller initializer"""
        
        self._view = view
        '''
        ### Temporary
        ###self._view.variableNums.currentIndexChanged.connect(self._view.variablesLayout.setCurrentIndex)
        ###self._view.first.csvInputBtn.clicked.connect(self.getFile)

        # Connect Paramaters
        self._view.bootstraps.textChanged.connect(partial(self._model._updateParamaters, "Bootstraps"))
        self._view.confidenceInterval.currentTextChanged.connect(partial(self._model._updateParamaters, "Confidence_Interval"))
        self._view.tcfe.currentTextChanged.connect(partial(self._model._updateParamaters, "TCFE"))
        self._view.comparisons.currentTextChanged.connect(partial(self._model._updateParamaters, "Correction_Type"))

        # Connect Analysis button
        self._view.analysisBtn.clicked.connect(self._model._createAnalysisFile)
        '''
    def getFile(self):
        file_filter = 'Data File (*.csv)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File (*.csv)'
        )
        print(response)
