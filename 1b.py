import csv
num_att = 6;
a=[]

print("\n the given training data set \n")

with open("enjoysport.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        reader.line_num
        if(row[0]!='sky'):
            a.append(row)
            print(row)

print("\n initial hyphothesis \n")
hyphothesis = ['0']*num_att
print(hyphothesis)

for j in range(0,num_att):
    hyphothesis[j] = a[0][j]

for i in range(0,len(a)):
    if a[i][num_att]=='yes':
        for j in range(0,num_att):
            if a[i][j] != hyphothesis[j]:
                hyphothesis[j]='?'
            else:
                hyphothesis[j]=a[i][j]

print("\n the maximally specific hyphothesis for a given training examples: \n")
print(hyphothesis)