# CSI4900_Honours_MediationModeration
4th year honours project Winter 2022 - Mediation and Moderation analysis of cognitive reserve

Supervisor: 
Jason Steffener 

Team members:
Matthew Tran 300028206
Alexandre Latimer 300027473

## About the project
This tool is created for the data input/prepocessing section of the [Mediation and Moderation](https://ncmlab.github.io/MediationModerationNotes/) project. It outputs an analysis file that will be used in the analysis section.

### Built with
* [PyQT5](https://pypi.org/project/PyQt5/)

### Prerequisites
* PyQT5
    ```pip install pyqt5```
* Pandas
    ```pip install pandas```
* Numpy
    ```pip install numpy```
* Nibabel
    ```pip install nibabel```

## Usage
##### Run main tool
To run the data input tool, run main.py. You will be prompted to chose a model setup file that can be found in the Models folder. Next you can fill in the data and create an analysis output file.

##### Creating setup file models
Help with creating setup file models can be found in the Models folder's README and more information on models can be found here: [Mediation and Moderation](https://ncmlab.github.io/MediationModerationNotes/)

##### Example read analysis file
read_analysis.py is an example file on how to read the analysis output file. Simply change the filepath string to the analysis output file filepath to test it out.