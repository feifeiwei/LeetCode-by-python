'''
给定一个表示分数的数组，预测玩家1是否会成为赢家。
你可以假设每个玩家的玩法都会使他的分数最大化。
输入: [1, 5, 2]
输出: False

输入: [1, 5, 233, 7]
输出: True
'''

###递归
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if self.momo(nums, 0, len(nums)-1) >= 0:
            return True
        return False
        
    
    def momo(self, nums, start, end):
        if start == end:
            return nums[start]
        
        return max(nums[start]-self.momo(nums,start+1,end),nums[end]-self.momo(nums,start, end-1))

###动态规划
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n==0 or n==1:
            return True
        dp = [[0]*n for i in range(n)]
        dp[n-1][n-1] = nums[n-1]
        
        for left in range(n-1,-1,-1):
            for right in range(left, n):
                if left==right:
                    dp[left][right] = nums[left]
                else:
                    l = nums[left] -  dp[left+1][right]
                    r = nums[right] - dp[left][right-1]
                    dp[left][right] = max(l,r)
                    
        return dp[0][n-1]>=0
                  
        
        
        
        
        
        
