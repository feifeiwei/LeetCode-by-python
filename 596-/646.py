'''
Created on Fri Aug 31 14:31:22 2018


1.每一个数对中，第一个数字总是比第二个数字小。
2.跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。

[[1,2], [2,3], [3,4]]
输出: 2
解释: 最长的数对链是 [1,2] -> [3,4]
@author: 60236
'''


class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        s = sorted(pairs,key=lambda x:x[1])
        ret = []
        
        for item in s:
            if len(ret)==0 or ret[-1][1] < item[0]:
                ret.append(item)
        return len(ret)
 
class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        s = sorted(pairs,key=lambda x:x[1])
        a,b = float('-inf'), 0
        for i in s:
            if a < i[0]:
                a = i[1]
                b += 1
        return b
