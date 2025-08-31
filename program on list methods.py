my_list=[10,20,10,30,40,50]
a=int(input("choose any list operation given billow:\n1.len()\n2.insert()\n3.append()\n4.copy\n5.extend\n6.remove()\n7.pop()\n8.Sort()\n9.reverse()\n10.clear()\n11.count\nnenter your choice:"))
if(a==1):
  n=len(my_list)
  print("No of elements in the list:")
elif(a==2):
  n=int(input("enter the element to insert:"))
  m=int(input("enter another element to insert:"))
  my_list.insert(n,m)
  print("after inserting the element:",my_list)
elif(a==3):
  a=int(input("enter the element to be append:"))
  my_list.append(a)
  print("after appending :",my_list)
elif(a==4):
  my_list1=my_list.copy()
  print("After copying  my_list1:",my_list)
elif(a==5):
   my_list.extend(my_list1)
   print("after extending my_list and my_list1:",my_list)
elif(a==6):
   n=int(input("enter the element to be removed;"))
   if(n in list):
       my_list.remove(n)
       print("after removing the element:",my_list)
   else:
       print("the element is not in the list.....")
elif(a==7):
    my_list.pop()
    print("after poping the list:",my_list)
elif(a==8):
    my_list.sort()
    print("after sorting the list:",my_list)
elif(a==9):
    my_list.reverse()
    print("after reversing the list:",my_list)
elif(a==10):
    my_list.clear()
    print("after clearing the list:",my_list)
elif(a==11):
    n=int(input("enter the number to find:"))
    my_list.count(n)
    print("No of times item",n,"found the list:",my_list)
else:
    print("invalid choice........")
          
       
  
  
