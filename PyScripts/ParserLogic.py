def isTotalStockHoldersEquity(aspect):
    if(aspect == "total stockholders' equity" or aspect == "total equity"):
        return True
    elif((("total stockholders' equity" in aspect) or ("total stockholders’ equity" in aspect)) and not ("total liabilities" in aspect)):
        return True
    return False