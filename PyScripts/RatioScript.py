import csv
import math
with open('PyScripts/HasData.csv') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    print(row) 
    #TODO make a dictionary with key value pairs and output that wit this script
    #TODO also make into a function where you call it using a file directory