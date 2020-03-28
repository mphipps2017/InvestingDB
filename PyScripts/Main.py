import RatioScript
import urllib.request
import os
ticker = input("CompanyTicker:\n")
#if(fileDirectory == ""):
    #fileDirectory = "Financial_Report.xlsx"
fileDirectory = os.getcwd() +"/Financial_Report.xlsx"
htmlUrl = urllib.request.urlopen("https://www.sec.gov/cgi-bin/browse-edgar?CIK="+ticker+"&action=getcompany&owner=exclude")
htmlDoc = htmlUrl.read().splitlines()
found = False
tenK = False
url = ""
i = 0
while (not found) and (i < len(htmlDoc)):
    if(not tenK and "10-K" in str(htmlDoc[i])):
        tenK = True
    elif(tenK and "/Archives/edgar/data/" in str(htmlDoc[i])):
        url = htmlDoc[i]
        found = True
    i = i + 1
splitUrl = str(url).split('/')
url = ""
for i in range(len(splitUrl)):
    if(splitUrl[i] == "data"):
        url = splitUrl[i+1] + "/"+splitUrl[i+2]
        break
url ="http://sec.gov/Archives/edgar/data/"+url+"/Financial_Report.xlsx"
urllib.request.urlretrieve(url, fileDirectory)
name = RatioScript.getRatios(fileDirectory)
os.remove(fileDirectory)
print("Success!\nDump: "+name+" created!")