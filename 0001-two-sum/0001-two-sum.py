class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_vals={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in dict_vals:
                return [dict_vals[diff],i]
            dict_vals[num]=i