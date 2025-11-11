class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_num=0
        for i in nums:
            xor_num^=i
        rightmost=(xor_num&(xor_num-1))^xor_num
        b1,b2=0,0
        for i in nums:
            if rightmost&i:
                b1^=i
            else:
                b2^=i
        return [b1,b2]