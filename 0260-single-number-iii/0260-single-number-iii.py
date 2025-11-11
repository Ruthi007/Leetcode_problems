class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count_dict={}
        res=[]
        for i in nums:
            count_dict[i]=count_dict.get(i,0)+1
        for key,value in count_dict.items():
            if value==1:
                res.append(key)
        return res
