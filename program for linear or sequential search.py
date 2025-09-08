def ssearch(alist,item):
    pos=0
    found=False
    stop=False
    while pos< len(alist) and not found and not stop:
        if alist[pos]==item:
            found=True
            print("element found in the list at position:",pos)
        else:
            if alist[pos]>item:
                stop=true
            else:
                pos=pos+1
    return found
a=[]
n=int(input("enter upper limit:"))
for i in range(n):
    a.append(int(input()))
x=int(input("enter element to search in the list:"))
ssearch(a,x)
