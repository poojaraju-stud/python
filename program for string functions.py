a=int(input(" choose any of the given \n1.boolean function on numbes and strings\n2.string function of different type of string\nenter your choice:"))
if(a==1):
    num="5"
    letters="abcdef"
    print(num.isnumeric())
    print(letters.isnumeric())
elif(a==2):
    computer="2024-2025-PYTHON"
    physics="Engineering Physics"
    drawing="engineering drawing"
    print(computer.islower())
    print(computer.isupper())
    print(physics.isupper())
    print(physics.istitle())
    print(drawing.istitle())
    print(drawing.islower())
else:
    print("existing.........")
    
    
                
