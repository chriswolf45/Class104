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
total = 0
for x in newdata:
    total+=x
mean =  total/n
print ("mean or average is"+ str(mean))