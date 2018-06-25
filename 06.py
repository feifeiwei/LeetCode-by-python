'''
Z字形变换
输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I

'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        L = ['']*numRows
        step = 1
        index = 0
        for  x in (s):
            
            L[index] += x
            
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1 
            index += step
            
        return ''.join(L)
