class Solution:
    def trap(self, height: list[int]) -> int:
        l,r=0,len(height)-1
        maxl,maxr=height[l],height[r]
        if not height: 
            return 0
        total=0
        while l<r:
            if height[l]<height[r]:
                maxl=max(maxl,height[l])
                total+=maxl-height[l]
                l+=1
            else:
                maxr=max(maxr,height[r])
                total+=maxr-height[r]
                r-=1
        return total

