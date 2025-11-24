class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float("inf")
        sum_val=0
        l=0
        for r in range(len(nums)):
            sum_val+=nums[r]
            while sum_val>=target:
                min_len=min(r-l+1,min_len)
                sum_val-=nums[l]
                l+=1
        return 0 if min_len==float("inf") else min_len
        
            