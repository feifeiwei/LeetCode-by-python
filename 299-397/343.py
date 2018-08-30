'''

给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 
返回你可以获得的最大乘积。

10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

思路：  把整数划分了 无限个 3 相乘，  整数最后剩余的要大于4


'''


class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        p = 1
        while n > 4:
            p *= 3
            n -= 3
        p *= n
        
        return p
    
    ###动态规划
    
    ##从1 到 n 存储 每一位的最大的乘机和
    class Solution:
        def integerBreak(self, n):
            """
            :type n: int
            :rtype: int
            """
            dp = [1]*(n+1)

            for i in range(2, n+1):
                for j in range(1,i):

                    dp[i] = max(dp[i], j*max(i-j, dp[i-j]))

            return dp[n]
