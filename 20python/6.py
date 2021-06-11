
s = input("輸入值為:")

a = s.split(",")#切割字串成串列

a.sort()#由小到大排序
g=""
for p in a:#取出串列每個元素
    g+=p #把串列組成字串 


a.sort(reverse=True)#由大到小排序 
max_str=""
for p in a:#取出串列每個元素
    max_str+=p #把串列組成字串

min_num=int(g)
max_num=int(max_str)
num=max_num-min_num
print(int(num))

#-int(min_str)#轉成整數後相減




