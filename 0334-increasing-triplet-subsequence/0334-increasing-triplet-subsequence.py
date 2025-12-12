class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1=n2=float('inf')
        for n in nums:
            if n<=n1:
                n1=n   # smallest value i
            elif n<=n2:
                n2=n   # second smallest value j
            else:
                return True 
        return False
