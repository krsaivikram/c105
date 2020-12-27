import csv
import math
with open("C:/Users/Manorama/downloads/data.csv",newline="") as f:
    reader = csv.reader(f)
    filedata = list(reader)
    data = filedata[0]
#Finding the mean
def Mean(data):
    n=len(data)
    total = 0
    for x in data:
        total = total+int(x)
    mean = total/n
    return mean
    #Squaring and getting the values
squaredlist = []
for number in data:
    a = int(number)- Mean(data)
    a = a**2
    squaredlist.append(a)
    #Getting the sum
sum = 0
for i in squaredlist:
    sum = sum+i
    #Dividing the sum by total value
result = sum/(len(data)-1)
#Taking a sqrt
standarddeviation = math.sqrt(result)
print(standarddeviation)                   
