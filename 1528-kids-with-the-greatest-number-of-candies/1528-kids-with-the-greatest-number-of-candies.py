class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c=max(candies)
        res=[]
        for i in candies:
            if (i+extraCandies)>=max_c:
                res.append(True)
            else:
                res.append(False)
        return res 