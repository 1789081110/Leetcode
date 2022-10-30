def LinearSearch(list1,n,key):
    for i in range(0,n):
        if list1[i]==key:
            return i
    return -1
list1=[1,2,3,4]
key=3 
n=len(list1)
res=LinearSearch(list1,n,key)
if res==-1:
    print(-1)
else:
    print(res)       
    
  
   # Output:2
