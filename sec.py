a=[]
b=int(input("Enter no of elements="))

for i in range(0,b):
    t=int(input("Enter in list="))
    a.append(t)

mini=a[0]
smin=0
for i in range(len(a)):
    if (a[i]>mini):
        smin=mini
        mini=a[i]
if(mini==a[0]):
    smin=mini

print(smin)
