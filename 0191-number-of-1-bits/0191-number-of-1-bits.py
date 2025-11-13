class Solution:
    def hammingWeight(self, n: int) -> int:
        res=''
        while n>0:
            if n%2==0:
                res+='0'
                n/=2
            elif n%2!=0:
                res+='1'
                n-=1
        count=0
        for i in res:
            if i=='1':
                count+=1
        return count

        