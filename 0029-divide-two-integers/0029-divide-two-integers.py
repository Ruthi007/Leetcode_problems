class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=0
        if (dividend==divisor): return 1
        sign=1
        if (dividend<0) ^ (divisor<0):
            sign=-1
        n=abs(dividend)
        d=abs(divisor)
        while(n>=d):
            count=0
            while (n >= d<<(count+1)):
                count+=1
            res+=1<<count
            n-=(d*1<<count)
        res=res if sign>0 else -res
        INT_MAX= (2**31)-1
        INT_MIN= -(2**31)
        if res<INT_MIN:
            return INT_MIN
        if res>INT_MAX:
            return INT_MAX
        return res
