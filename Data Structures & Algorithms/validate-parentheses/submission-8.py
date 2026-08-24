class Solution:
    def isValid(self, s: str) -> bool:
        mapping={"(":")","[":"]","{":"}"}
        stack=[]

        for char in s:
            if char in mapping.keys():
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                if char==mapping[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack):
            return False
        return True
                    