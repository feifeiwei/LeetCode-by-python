'''
输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。

'''


class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [ [0]*(len(s2)+1) for i in range(len(s1)+1)]


        for j in range(1,len(s2)+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        

        for i in range(1,len(s1)+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min( dp[i][j-1]+ord(s2[j-1]), dp[i-1][j]+ord(s1[i-1])  )
        return dp[len(s1)][len(s2)]
