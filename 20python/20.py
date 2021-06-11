T=[["123","Tom","DGTD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","WON","FDD"]]

a=input("輸入查詢學號為:")

for r in T:
    #print(r)
    if (r[0]==a):
        v=" ".join(r)
        print("學生資料為:",v)

