# Creating a Model Setup File
Model setup files include these variables:

##### ModelName 
A string representing the name of the model.

##### Direct 
A matrix representing the direct effect of a variable to another. 1 represents an effect while 0 represents no effect. For more information, see [here](https://ncmlab.github.io/MediationModerationNotes/The_direct_effects_matrix)

##### Interaction*
A matrix representing an interaction of variables to predict a variable. A row with 2 or more 1s represent interacting variables while 0 represents no interaction. For more information, see [here](https://ncmlab.github.io/MediationModerationNotes/The_interaction_terms)

##### Path
A matrix representing the steps in the paths of the direct matrix effect matrix. This means they have an identical setup but different values. For more information, see [here](https://ncmlab.github.io/MediationModerationNotes/The_path_matrix)

##### Out
A string array the size of the number of variables in the model. It represents the outcome variable that are directly effected by another variable. If a variable is not an outcome variable, it is empty. For an example, see [here](https://ncmlab.github.io/MediationModerationNotes/Model_6)

##### In
An array of string arrays the size of the number of variables in the model. Each array represent what variables have an effect on a variable (direct or indirect). For an example, see [here](https://ncmlab.github.io/MediationModerationNotes/Model_6)

##### Inter
An array of arrays the size of the number of variables in the model. This represents the effect of n-way interactions on a variable. For an example, see [here](https://ncmlab.github.io/MediationModerationNotes/Model_5)



**\* is not required if not present**