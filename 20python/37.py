
n = int(input(""))

for i in range(n) :
    k = int(input(""))
    if(k >=1 and k <= 1000):
         if(k%9==0 or k %11==0):
            print("第"+str(i) +"個點"+str(k)) 



