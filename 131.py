'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。
'''

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = []
        
        def dum(s,cur):
            if len(s)==0:
                ret.append(list(cur))
            
            for i in range(len(s)):
                tmp = s[:i+1]    
                if tmp == tmp[::-1]:
                    cur.append(tmp)
                    dum(s[i+1:],cur)
                    cur.pop()
        dum(s,[])
        
        return ret
                
