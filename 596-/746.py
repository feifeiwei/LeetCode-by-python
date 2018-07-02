'''
使用最小花费爬楼梯
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
你可以选择继续爬一个阶梯或者爬两个阶梯。

'''
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        a,b = cost[0], cost[1]
        l = len(cost)
        if l <= 1:
            return 0
        
        for i in range(2,l):
            a,b = b, min(a,b)+cost[i]
        return min(a,b)
            
