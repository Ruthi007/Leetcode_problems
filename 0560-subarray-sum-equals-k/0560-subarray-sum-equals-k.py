class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefixsum={0:1}
        cursum=0
        for i in nums:
            cursum+=i
            diff=cursum-k
            count+=prefixsum.get(diff,0)
            prefixsum[cursum]=1+prefixsum.get(cursum,0)
        return count