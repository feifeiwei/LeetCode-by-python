'''

计算这个字符串中有多少个回文子串。

"aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

'''

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        for i in range(len(s)):
            n = self.ju(s,i,i)
            m += n
            n = self.ju(s,i,i+1)
            m += n
        
        return m
        
        
    
    def ju(self, s, i, j):
        n = 0
        
        while i>=0 and j < len(s) and s[i]==s[j]:
            i -= 1
            j += 1
            n += 1
        return n
