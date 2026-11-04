heights=[1,8,6,2,5,4,8,3,7]
left=0
right=len(heights)-1
max_area=0
while left<right:
    width=right-left
    height=min(heights[left],heights[right])
    area=width*height
    max_area=max(max_area,area)
    if heights[left]<heights[right]:
        left+=1
    else:
        right-=1
print(max_area)

#Approch2-BruteForce
heights=[1,8,6,2,5,4,8,3,7]
max_area=0
for i in range(len(heights)):
    for j in range(len(heights)):
        width=j-i
        height=min(heights[i],heights[j])
        area=width*height
        max_area=max(max_area,area)
print(max_area)

#approch3 -Optimized Two pointers

heights=[1,8,6,2,5,4,8,3,7]
left=0
right=len(heights)-1
max_area=0
while left<right:
    width=right-left
    height=min(heights[left],heights[right])
    area=width*height
    if area>max_area:
        max_area=area
    if heights[left]<heights[right]:
        left+=1
    else:
        right-=1
print(max_area)

#Approch3-Two pointers with best-pair tracking
heights=[1,8,6,2,5,4,8,3,7]
left=0
right=len(heights)-1
max_area=0
best_left=0
best_right=0
while left<right:
    width=right-left
    height=min(heights[left],heights[right])
    area=width*height
    if area>max_area:
        max_area=area
        best_left=left
        best_right=right
    if heights[left]<heights[right]:
        left+=1
    else:
        right-=1
print("Maximum Area:",max_area)
print("Best indices:",best_left,best_right)


