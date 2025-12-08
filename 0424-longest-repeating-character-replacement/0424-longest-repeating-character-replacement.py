class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chardict={}
        l=0
        res=0
        for r in range(len(s)):
            chardict[s[r]]=1+chardict.get(s[r],0)
            while (r-l+1) - max(chardict.values()) >k:
                chardict[s[l]]-=1
                l+=1
            res=max(res,(r-l+1))
        return res