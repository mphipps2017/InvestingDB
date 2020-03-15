import csv

#def getRatios(fileDirectory)
    #TODO When completed make it so this runs using the above method header
with open('PyScripts/HasData.csv') as csvfile:
reader = csv.reader(csvfile)
for row in reader:
    print(row) 