print("*press 1 to find current date and time\n*press 2 to find the calendar of given month\n*press 3 to exit")
a=int(input("\nenter your choice:"))
if(a==1):
    import datetime
    now=datetime.datetime.now()
    print("current date and time:")
    print(now.strftime("%Y-%m%d   %H:%M:%S"))
elif(a==2):
    import calendar
    y=int(input("input the year:"))
    m=int(input("input the month:"))
    print(calendar.month(y,m))
else:
    print("exited.............")
