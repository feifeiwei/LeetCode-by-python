'''
给定一个非负整数 num。 对于范围 0 ≤ i ≤ num 中的每个数字 i ，计算其二进制数中的1的数目并将它们作为数组返回。

示例：
比如给定 num = 5 ，应该返回 [0,1,1,2,1,2].
'''

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0]*(num+1)
        
        for i in range(num+1):
            ret[i] = i%2 + ret[i//2]
        return ret

class Solution2:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        offset = 1
        ret = [0]

        for i in range(1,num+1):
            if offset*2==i:
                offset *= 2
            
            ret.append(ret[i-offset]+1)
        return ret
