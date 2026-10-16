class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n=len(numbers)
        l,r=0,n-1
        while l<r:
            sum_val=numbers[l]+numbers[r]
            if sum_val==target:
                return [l+1,r+1]
            elif sum_val>target:
                r-=1
            else:
                l+=1
        return []
