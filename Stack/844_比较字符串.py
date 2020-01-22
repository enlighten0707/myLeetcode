class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1=[]
        stack2=[]
        for ch in S :
            if ch == '#':
                if stack1 :
                    stack1.pop()
            else :
                stack1.append(ch)

        for ch in T :
            if ch == '#':
                if stack2 :
                    stack2.pop()
            else :
                stack2.append(ch)
        
        if stack1[:]== stack2[:] :
            return True
        else :
            return False

        