class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping={}
        for i in range(len(nums2)):
            stack=[]
            for j in range(len(nums2)-1,i,-1):
                stack.append(nums2[j])

            if not stack:
                mapping[nums2[i]]=-1
                break
            
            ans=nums2[i]
            while(stack and ans <= nums2[i]):
                ans=stack.pop()
            
            if ans > nums2[i]:
                mapping[nums2[i]]=ans
            else:
                mapping[nums2[i]]=-1
        Ans=[]
        for num in nums1:
            Ans.append(mapping[num])
        
        return Ans

# 维护一个单调栈
# mapping映射
# 如果当前元素大于栈顶元素，出栈mapping,并且是所有出栈；否则，放到栈顶；最后留在栈中的映射到-1

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping={}
        stack=[] #数据栈
        for num in nums2 :
            while stack and num>stack[len(stack)-1]:
                mapping[stack.pop()]=num
            stack.append(num)
        
        while stack:
            tmp=stack.pop()
            mapping[tmp]=-1
        
        Ans=[]
        for idx,num in enumerate(nums1):
            Ans.append(mapping[num])
        return Ans



