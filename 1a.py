num=int(input("Enter the number;"))
val=str(num)
rev = val[::-1]
if (val==rev):
    print("Pal")
else:
    print("Not Pal")
    for i in range(10):
        if (val.count(str(i))>0):
    print(str(i),"appears",val.count(str(i)),"times")