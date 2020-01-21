class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        carry=1

        while(i>=0 and carry==1):
            if(digits[i]<9):
                digits[i]+=carry
                carry=0
            else:
                digits[i]=0
                carry=1
            i-=1

        if(i==-1 and carry==1):
            res=[]
            res.append(1)
            for j in range (len(digits)):
                res.append(digits[j])
            return res
        return digits
