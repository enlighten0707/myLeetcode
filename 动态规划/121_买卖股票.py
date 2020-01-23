class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxProfit=0
        curMin=prices[0]
        for i in range(1,len(prices)):
            curMin=min(curMin,prices[i])
            maxProfit=max(maxProfit,prices[i]-curMin)
        return maxProfit

# 另一种想法：求差数组的最大子序和=原数组的元素最大差 牛顿-莱布尼兹公式