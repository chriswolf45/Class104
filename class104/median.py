import csv
with open("height.weight.csv",newline="")as f:
    reader = csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
newdata=[]
for i in range(len(file_data)):
    n_nun = file_data[i][1]
    newdata.append(float(n_nun))
n= len(newdata)
newdata.sort()
if n% 2==0:
    median1 = float(newdata[n//2])
    median2 = float(newdata[n//2-1])
    median = (median1+median2)/2
else :
    median=newdata[n//2]
    print(n)
print("median is "+ str(median))
