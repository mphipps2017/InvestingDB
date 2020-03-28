import RatioScript
import urllib.request
import os
#fileDirectory = input("Data Directory:\n")
#if(fileDirectory == ""):
    #fileDirectory = "Financial_Report.xlsx"
fileDirectory = os.getcwd() +"/Financial_Report.xlsx"
#TODO Make this url dynamic (issue a get request and skim page for first occurence of 10-k and the skim page for first occurence ofdata/compname/doc#)
url ="http://sec.gov/Archives/edgar/data/20639/000114036119005745/Financial_Report.xlsx"
urllib.request.urlretrieve(url, fileDirectory)
name = RatioScript.getRatios(fileDirectory)
os.remove(fileDirectory)
print("Success!\nDump: "+name+" created!")