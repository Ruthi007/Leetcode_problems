class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum=cursum=sum(nums[:k])
        for i in range(len(nums)-k):
            cursum+=nums[i+k]-nums[i]
            if cursum>max_sum:
                max_sum=cursum
        return max_sum/k