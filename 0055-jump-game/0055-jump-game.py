class Solution:
    def canJump(self, nums: List[int]) -> bool:
            max_step=0
            for i in range(len(nums)):
                if i>max_step:
                    return False
                max_step=max(i+nums[i],max_step)
            return True
