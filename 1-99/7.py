'''
给定一个 32 位有符号整数，将整数中的数字进行反转。
7. 反转整数
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x>0 else -1
        x = -x if x < 0 else x
        rev = 0
        
        while x != 0:
            rev = 10*rev + x%10
            if rev > 2**31-1 or rev < -2**31:
                return 0
            x //= 10
            
    return rev*flag
