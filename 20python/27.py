a=input("甲方的數字:")
b=input("乙方的數字:")
c=""

nums1=len(a)
nums2=len(b)
if (nums1==nums2):
    for i in range(nums1) :
       if(int(a[i])>int(b[i])):
            c=c+"贏"
       if(int(a[i])<int(b[i])):
            c=c+"輸"
       if(int(a[i])==int(b[i])):
            c=c+"和"
else:
    print("error")    


print("洗刷刷結果:",c)    