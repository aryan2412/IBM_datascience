b=int(input("Enter no of elements="))

a=[int (i) for i in input("enter elements of list").strip().split()]

mini=a[0]
smin=0
for i in range(len(a)):
    if (a[i]>mini):
        smin=mini
        mini=a[i]
if(mini==a[0]):
    smin=mini

print(smin)
