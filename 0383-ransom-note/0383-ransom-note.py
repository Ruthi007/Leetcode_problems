class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m={}
        for i in magazine:
            m[i]=m.get(i,0)+1
        for i in ransomNote:
            if i in m and m[i]>0:
                m[i]-=1
            else:
                return False
        return True

        