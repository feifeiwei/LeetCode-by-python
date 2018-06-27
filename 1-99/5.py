'''
最长回文子串
输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        
        for i in range(len(s)):
            tmp = self.hel(s,i,i)
            if len(tmp) > len(ret):
                ret = tmp
        
            tmp = self.hel(s,i,i+1)
            if len(tmp) > len(ret):
                ret = tmp
        return ret
            
    def hel(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
return s[l+1:r]
