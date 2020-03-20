def isTotalStockHoldersEquity(aspect):
    if(aspect == "total stockholders' equity" or aspect == "total equity"):
        return True
    elif((("total stockholders' equity" in aspect) or ("total stockholders’ equity" in aspect)) and not ("total liabilities" in aspect)):
        return True
    return False

def getRowValue(row):
    ret = 0
    loop = 1
    i = 1
    while loop == 1 and i < len(row):
        try:
            ret = float(row[i].value)
            loop = 0
        except TypeError:
            loop = 1
            i = i + 1
    return ret
