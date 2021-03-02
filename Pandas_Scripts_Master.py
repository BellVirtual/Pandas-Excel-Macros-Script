import os
import sys
import pandas as pd


'getcwd:      ', os.getcwd()
osfile, maindir =('__file__:    ', __file__)
filename = os.path.basename(sys.argv[0])
inpath = maindir.replace(filename,"Excels")
outpath = maindir.replace(filename,"BulkFile.xlsx")






def read_xl_dir():
    for root, dirs, files in os.walk(inpath):
        for f in files:
            filepath = os.path.join(root, f)
            name, extension = os.path.splitext(filepath)
            if extension == '.xlsx':
                print(filepath)
                delete_coulms_all(filepath)




def compact_xl(filepath):
    excelframe = pd.read_excel(filepath)
    dataframes = [excelframe]
    compactframes = pd.concat(dataframes)
    compactframes.to_excel(outpath)


def delete_coulms_all(filepath):
    excelframe = pd.read_excel(filepath)
    del_frame = excelframe.drop(columns=['Discount Band'])
    dataframe = [del_frame]
    compactframe = pd.concat(dataframe)
    dirpath = filepath.replace("Excels","New_Excels")
    print(dirpath)
    compactframe.to_excel(dirpath)


def delete_coulms_one(filepath):
    excelframe = pd.read_excel(filepath)
    del_frame = excelframe.drop(columns=['Discount Band'])
    dataframe = [del_frame]
    compactframe = pd.concat(dataframe)
    compactframe.to_excel(outpath)

def add_column_one(filepath):
    excelframe = pd.read_excel(filepath)
    # if column is a number or need to be converted it has to be defined like
    # excelframe['num'].astype(str)
    #######addd funtion here
    excelframe['full_name'] = excelframe.first_name + " " + excelframe.last_name
    ####export data
    dataframe = [excelframe]
    compactframe = pd.concat(dataframe)
    compactframe.to_excel(outpath)


def add_column_all(filepath):
    excelframe = pd.read_excel(filepath)
    # if column is a number or need to be converted it has to be defined like
    # excelframe['num'].astype(str)
    #######addd funtion here
    excelframe['full_name'] = excelframe.first_name + " " + excelframe.last_name
    ####export data
    dataframe = [excelframe]
    compactframe = pd.concat(dataframe)
    dirpath = filepath.replace("Excels","New_Excels")
    print(dirpath)
    compactframe.to_excel(dirpath)



read_xl_dir()