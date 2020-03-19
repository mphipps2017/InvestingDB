import RatioScript
import os
fileDirectory = input("Data Directory:\n")
if(fileDirectory == ""):
    fileDirectory = "Financial_Report.xlsx"
fileDirectory = os.getcwd() +"/" +fileDirectory
name = RatioScript.getRatios(fileDirectory)
print("Success!\nDump: "+name+" created!")