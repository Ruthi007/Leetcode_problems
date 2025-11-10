class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        num_subsets=1<<n
        res=[]
        for i in range(num_subsets):     #for num of subsets
            possible_list=[]
            for j in range(n):           # checking if the bits are set or not
                if (i & 1<<j):
                    possible_list.append(nums[j])
            res.append(possible_list)
        return res