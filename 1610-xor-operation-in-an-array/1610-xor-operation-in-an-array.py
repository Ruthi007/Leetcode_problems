class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        res=0
        for i in range(n):
            nums.append(start+2*i)
        for i in nums:
            res^=i
        return res