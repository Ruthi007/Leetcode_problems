class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        clTOop={")":"(","}":"{","]":"["}
        for i in s:
            if i in clTOop:
                if stack and stack[-1]==clTOop[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False