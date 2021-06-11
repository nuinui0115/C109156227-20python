n=int(input(""))
b=n-3
for i in range(b):
    for j in range(b-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print("")
for i in range(b-1):
    for j in range(i+1):
        print(" ",end="")
    for k in range(2*(b-i)-3):
        print("*",end="")
    print("")

    
    
    
    
    
    
    
    
    
    
    
    