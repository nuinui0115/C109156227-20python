a=list(input("請輸入第一組數字:"))
b=list(input("請輸入第二組數字:"))
c=0
d=0
for i in range (len(a)):
    for j in range (len(b)):
        if a[i]==b[j] and i==j:
            c=c+1
        elif a[i]==b[j] and i!=j:
            d=d+1
if a[i]==b[j] and i==j:       
    print(str(c)+"A"+str(d)+"B","全對")
else:
    print(str(c)+"A"+str(d)+"B","加油")
