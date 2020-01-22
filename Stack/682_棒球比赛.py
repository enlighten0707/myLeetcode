# python 中将数字从str变成int，直接int(str)
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        #维护一个栈，记录每轮的得分，一个变量，记录当前总分
        stack=[]
        score=0
        for ch in ops :
            if ch == 'C':
                tmp=stack.pop()
                score-=tmp
            elif ch == 'D':
                tmp= 2*stack[len(stack)-1]
                stack.append(tmp)
                score+=tmp
            elif ch == '+':
                tmp=stack[len(stack)-1]+stack[len(stack)-2]
                stack.append(tmp)
                score+= tmp
            else:
                stack.append(int(ch))
                score+=int(ch)
        return score
