'''
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
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
            
