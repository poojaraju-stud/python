a=int(input("choose any type of operator given above\n1.relational operator\n2.arithmatic operator\n3.logical operator\n4.Assignment operator\n5.bitwise operator\n6.membership operator\n7.identity operator\n press 0 to exist...\nenter your choice:"))
if(a==2):
      print("your choice is arithmetic operator...........\n")
      n1=int(input("enter the value of n1:"))
      n2=int(input("enter the value of n2:"))
      sum=a+b;
      sub=a-b;
      mul=a*b;
      div=a/b;
      rem=a%b;
      print("sum=",sum)
      print("sub=",sub)
      print("mul=",mul)
      print("div=",div)
      print("rem=",rem)
elif(a==1):
    print("your choice is relational operator..........")
    x=int(input("enter the value of x:"))
    y=int(input("enter the value of y:"))
    if(x==y):
        print("x is equal to y")
    elif(x!=y):
        print("x is not equal to y")
    elif(x<y):
        print("y is greater than x")
    elif(x>y):    
        print("x is greater than y")
    elif(x<=y):
        print("x is lessthan or equal to y")
    elif(x>=y):
        print("x is greaterthan or equal to y")
    else:
        print("invalid....")
elif(a==3):
    print("your choice is logical operator.....")
    c1=int(input("enter the value of c1:"))
    c2=int(input("enter the value of c2:"))
    c3=int(input("enter the value of c3:"))
    if(c1<c2)and(c1<c3):
        print("\n c1 is lessthan c2 and c3")
    if(not(c1<c2)):
        print("\nc1 is greaterthan c2")
    if((c1<c2)or(c1<c3)):
        print("\n c1 is lessthan c2 or c3 or both")
elif(a==4):
    print("your choice is Assignment opertator.....")
    x=20
    y=10
    z=0
    z=X+y
    print("value of z is",z)
    z+=y
    print("value of z is",z)
    z/=x
    print("value of z is",z)
    z=2
    z%=x
    print("value of z is",z)
    z**=x
    print("value of z is",z)
    z//=x
    print("value of z is",z)
elif(a==5):
    print("your choice is Bitwise operator....")
    x=62
    y=11
    z=0
    z=x&y;
    print("the value of z is",z)
    z=x|y;
    print("the value of z is",z)
    z=x^y;
    print("the value of z is",z)
    z=x<<2;
    print("the value of z is",z)
    z=x>>2;
    print("the value of z is",z)
elif(a==6):
    print("your choice is membership operator......")
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    list=[1,2,3,4,5];
    if(x in list):
        print("x is in given list")
    else:
        print("x is not in given list")
    if(y not in list):
        print("y is not in given list")
    else:
        print(" y is in given list")
elif(a==7):
    print("your choice is identity operator......")
    x=int(input("enter x value:"))
    y=int(input("enter y value:"))
    if(x is y):
          print("x and y have same identity")
    else:
         print("x and y not have same identity")
    if(id(x)==id(y)):
        print("x and y have same identity")
    else:
         print("x and y not have same identity")
         
else:
    print("exist..........")
    
    
    

    
      
