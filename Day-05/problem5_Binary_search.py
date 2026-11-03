l=[10,20,30,40,50,60,70]
target=40
left=0
right=len(l)-1
while left<right:
    mid=(left+right)//2
    if l[mid]==target:
        print("Element is found at index",mid)
        break
    elif l[mid]<target:
        left=mid+1
        
    else:
        right=mid-1
else:
    print("Element is not found")
        