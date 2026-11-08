class Solution:
    def findMaxAverage(self, nums, k):
        max_average = float('-inf')

        for i in range(len(nums) - k + 1):
            current_sum = 0

            for j in range(i, i + k):
                current_sum += nums[j]

            average = current_sum / k

            if average > max_average:
                max_average = average

        return max_average