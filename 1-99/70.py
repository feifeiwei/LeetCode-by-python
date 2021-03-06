'''
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n<=1:
            return 1
        
        if n > 1:
            a, b = 0, 1
            while n >= 1:
                a,b = b,a+b
                n -= 1
            return b
