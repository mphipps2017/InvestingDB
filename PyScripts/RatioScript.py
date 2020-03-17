import csv
import ParserLogic

def getRatios(dataDirectory, companyName, companyTicker):
    with open(dataDirectory) as csvfile:
        reader = csv.reader(csvfile)
        totalAssets = 0.0
        totalLiabilities = 0.0
        totalEquity = 0.0
        currentLiabilities = 0.0
        currentAssets = 0.0
        cash = 0.0
        treasuryStock = 0
        totalEquity = 0.0
        revenue = 0.0
        earnings = 0.0
        # Parse input data
        for row in reader:
            aspect = row[0].lower()
            if(aspect == 'total assets'):
                totalAssets = float(row[1])
            elif("total liabilities" == aspect):
                totalLiabilities = float(row[1])
            elif(aspect == 'total current liabilities'):
                currentLiabilities = float(row[1])
            elif("cash" in aspect):
                cash = float(row[1])
            elif(aspect == 'total current assets'):
                currentAssets = float(row[1])
            elif("treasury stock" in aspect):
                treasuryStock = int(row[1])
            elif(ParserLogic.isTotalStockHoldersEquity(aspect)):
                totalEquity = float(row[1])
            elif(aspect == "net revenues" or aspect == "total revenues" or aspect == "operating revenues" or aspect == "net sales"):
                revenue = float(row[1])
            elif(aspect == "net earnings" or aspect == "net loss" or aspect == "net income"):
                earnings = float(row[1])
    # Calculate Ratios
    if(totalEquity == 0 and totalLiabilities != 0):
        totalEquity = totalAssets-totalLiabilities
    if(totalLiabilities == 0 and totalAssets != 0 and totalEquity != 0):
        totalLiabilities = totalAssets - totalEquity 
    #print("Equity: "+str(totalEquity)+"\nLiabilties: "+str(totalLiabilities)+"\nAssets: "+str(totalAssets))
    debt_to_assets = totalLiabilities/totalAssets
    longTermLiabilities = totalLiabilities - currentLiabilities
    longtermDE = longTermLiabilities/totalEquity
    debt_to_equity = totalLiabilities/totalEquity
    cashRatio = cash/currentLiabilities
    current_Ratio = currentAssets/currentLiabilities
    if(revenue == 0):
        netPorfitMargin = "Rev was 0"
    else:
        netPorfitMargin = earnings/revenue

    # Print output file
    dumpName = companyTicker + "dump.csv"
    with open(dumpName, 'w', newline='') as dumpFile:
        writer = csv.writer(dumpFile)
        writer.writerow(["Company", companyName])
        writer.writerow(["Ratio", "Value"])
        writer.writerow(["Cash Ratio", str(cashRatio)])
        writer.writerow(["Current Ratio", str(current_Ratio)])
        writer.writerow(["Debt-to-assets Ratio", str(debt_to_assets)])
        writer.writerow(["Debt-to-equity Ratio", str(debt_to_equity)])
        writer.writerow(["Longterm DE", str(longtermDE)])
        writer.writerow(["Treasury Stock", str(treasuryStock)])
        writer.writerow(["Net Profit margin", str(netPorfitMargin)])