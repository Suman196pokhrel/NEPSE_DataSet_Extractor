# NEPSE_DataSet_Extractor
This is a python desktop Application,
used to extract Specific Company Dataset from thousands of csv files
present in the various Folders inside the standard Kaggle Nepal-stock-exchange-dataset, 
and create a unique csv file for only one selected company,

Tools Used:
1) Python Language
2) PyQt5 Module
3) Pandas Moduel
4) Threading Module
5) Os Module
6) Time Module

7) Qt-Designer For Rapid UI-development

Description About The Project:
=> I was Searching the internet for Nepal-Stock-Exchange's Complete Dataset,and as always 
i found a complete dataset form 2012- 2020/03 in [Kaggle](https://www.kaggle.com/sagyamthapa/nepali-stock-market-form-2012-to-2020-till-march?select=Nepali_Stock_Market+_Data__2012-2020)
But now that i had downloaded the dataset and was looking through it
, i found that the data was unstructured. In each folder for example 2012,
there were 900+ csv files , that had the data of each company on that specific day.
So each csv files had multiple Company names and their multiple columns,But for data visualization of a single company i needed 
a complete dataset of a SINGLE company from Start-End , 

And Thus i thought of this project ,User possibly cannot go to each csv file in each folder
and copy a specific row and paste it into a new csv file,There are more than 700+ csv files in single 
folder and there are total 9 of these folders.
This project provides a GUi interface to the user 
for providing path to Main Dataset-Folder and Location where you want to save the
newly extracted dataset for a single company,

The resulting-dataset/ Extracted Dataset  would be a loot easy to work with while data-Visualization tasks 
or as an ML dataset. 

NOTE:

=> Applicaiton still consists of small bugs that need to be cleaned

=> Do not leave the MainPath and ToSave textField Empty and press Extract Button, it would simply crah,

=>For now, The Application only saves the file in csv format, so you will have to specify the .csv extension while choosing the SaveTo path
example:(c:\..\...\...\example.csv)

Images of Working Application:

MainWindow :
![mainWin.PNG](https://github.com/Suman196pokhrel/NEPSE_DataSet_Extractor/blob/master/mainWin.PNG)

Working Window:
![working.PNG](https://github.com/Suman196pokhrel/NEPSE_DataSet_Extractor/blob/master/working.PNG)

