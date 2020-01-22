# Stack is a List ---- stack.append /stack.pop
# 括号匹配问题，最后考虑剩下的括号
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        #build map to make the code clean

        mapping={")":"(","}":"{","]":"["}

        for ch in s:
            if (ch in mapping ):
                if len(stack)==0 :
                    return False
                top_ele=stack.pop()
                if(top_ele != mapping[ch]):
                    return False
            else:
                stack.append(ch)
        
        return not stack
