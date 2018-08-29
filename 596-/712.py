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

    ###思路2
    
    ## s1,s2   找到 s2, s1 最多公共部分  然后  s2+s1 - 2*(公共部分)
    class Solution:
        def minimumDeleteSum(self, s1, s2):
            """
            :type s1: str
            :type s2: str
            :rtype: int
            """
            l = max(len(s1), len(s2))
            if len(s1) != l:
                s1, s2 = s2,s1
            dummy = [0] * (len(s2)+1)

            for i in range(1,len(s1)+1):  
                tmp = [0]
                for j in range(1,len(s2)+1):
                    if s1[i-1] == s2[j-1]:
                        tmp.append(dummy[j-1] + ord(s1[i-1]))
                    else:
                        tmp.append(max(tmp[-1], dummy[j]))
                dummy = tmp[:]
            return sum(map(ord,s1+s2)) - 2*dummy[-1]

        
