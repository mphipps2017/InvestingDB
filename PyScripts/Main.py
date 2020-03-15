import RatioScript
fileDirectory = input("Data Directory:\n")
companyName   = input("Compnay name:\n")
companyTicker = input("Company Ticker:\n")
RatioScript.getRatios(fileDirectory, companyName, companyTicker)