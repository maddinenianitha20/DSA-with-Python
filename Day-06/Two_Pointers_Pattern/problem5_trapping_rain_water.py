heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

left = 0
right = len(heights) - 1

left_max = 0
right_max = 0

water = 0

while left < right:

    if heights[left] < heights[right]:

        if heights[left] >= left_max:
            left_max = heights[left]
        else:
            water += left_max - heights[left]

        left += 1

    else:

        if heights[right] >= right_max:
            right_max = heights[right]
        else:
            water += right_max - heights[right]

        right -= 1

print(water)

#Approch2-BruteForce

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

water = 0

for i in range(len(heights)):
    left_max = max(heights[:i + 1])
    right_max = max(heights[i:])

    trapped = min(left_max, right_max) - heights[i]
    water += trapped

print(water)