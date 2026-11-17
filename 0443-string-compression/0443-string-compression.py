class Solution:
    def compress(self, chars: list[str]) -> int:
        i=0
        insert=0
        while i<len(chars):
            grp=1
            while (grp+i)<len(chars) and chars[grp+i]==chars[i]:
                grp+=1
            chars[insert]=chars[i]
            insert+=1
            if grp>1:
                num_str=str(grp)
                chars[insert:insert+len(num_str)]=list(num_str)
                insert+=len(num_str)
            i+=grp
        return insert
