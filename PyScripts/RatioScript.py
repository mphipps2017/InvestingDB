import csv

#def getRatios(fileDirectory)
    #TODO When completed make it so this runs using the above method header
with open('PyScripts/HasData.csv') as csvfile:
    reader = csv.reader(csvfile)
    totalAssets = 0.0
    totalLiabilities = 0.0
    totalEquity = 0.0
    currentLiabilities = 0.0
    currentAssets = 0.0
    cash = 0.0
    treasuryStock = 0
    for row in reader:
        aspect = row[0].lower()
        if(aspect == 'total assets'):
            totalAssets = float(row[1])
        elif(aspect == 'total liabilities'):
            totalLiabilities = float(row[1])
        elif(aspect == 'total current liabilities'):
            currentLiabilities = float(row[1])
        elif(aspect == 'cash and cash equivalents'):
            cash = float(row[1])
        elif(aspect == 'total current assets'):
            currentAssets = float(row[1])
        elif("treasury stock" in aspect):
            treasuryStock = int(row[1])
    #TODO Make it calculate net profit margin
        
    totalEquity = totalAssets-totalLiabilities
    debt_to_assets = totalLiabilities/totalAssets
    longTermLiabilities = totalLiabilities - currentLiabilities
    longtermDE = longTermLiabilities/totalEquity
    debt_to_equity = totalLiabilities/totalEquity
    cashRatio = cash/currentLiabilities
    current_Ratio = currentAssets/currentLiabilities

with open('dump.csv', 'w', newline='') as dumpFile:
    writer = csv.writer(dumpFile)
    writer.writerow(["Ratio", "Value"])
    writer.writerow(["Cash Ratio", str(cashRatio)])
    writer.writerow(["Current Ratio", str(current_Ratio)])
    writer.writerow(["Debt-to-assets Ratio", str(debt_to_assets)])
    writer.writerow(["Debt-to-equity Ratio", str(debt_to_equity)])
    writer.writerow(["Longterm DE", str(longtermDE)])
    writer.writerow(["Treasury Stock", str(treasuryStock)])