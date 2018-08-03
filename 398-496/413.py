'''
A = [1, 2, 3, 4]

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。

'''

class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cur = 0
        s = 0
        for i in range(2,len(A)):
            
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                cur += 1
                s+= cur
            else:
                cur = 0
        return s
