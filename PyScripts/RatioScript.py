import csv

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
            elif(aspect == "total shareholders' equity" or aspect == "total stockholders' equity"):
                totalEquity = float(row[1])
            elif(aspect == "net revenues" or aspect == "total revenues"):
                revenue = float(row[1])
            elif(aspect == "net earnings" or aspect == "net loss"):
                earnings = float(row[1])
    # Calculate Ratios
    if(totalEquity == 0 and totalLiabilities != 0):
        totalEquity = totalAssets-totalLiabilities
    debt_to_assets = totalLiabilities/totalAssets
    longTermLiabilities = totalLiabilities - currentLiabilities
    longtermDE = longTermLiabilities/totalEquity
    debt_to_equity = totalLiabilities/totalEquity
    cashRatio = cash/currentLiabilities
    current_Ratio = currentAssets/currentLiabilities
    if(revenue == 0):
        netPorfitMargin = 0
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