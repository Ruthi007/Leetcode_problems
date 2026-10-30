class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numbers=set(nums)
        longest=0
        for i in numbers:
            if (i-1) not in numbers:
                length=0
                while(length+i) in numbers:
                    length+=1
                longest=max(length,longest)
        return longest
