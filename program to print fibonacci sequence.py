n=int(input("enter maximum limit:"))
n1=0
n2=1
count=2

if n<=0:
    print("please enter a positive integer")
elif n==1:
    print("fibanacci sequence upto",n,":")
    print(n1)
else:
    print("fibanacci sequence upto",n,":")
    print(n1,",",n2,end=' ')
    while count < n:
       nth = n1+n2
       print(nth,end=',')
       n1=n2
       n2=nth
       count+=1
