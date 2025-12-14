class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq=[]
        for i in nums:
            sq.append(i**2)
        return sorted(sq)
        #in one line sq=[i**2 for i in nums]
        #return sorted(sq)