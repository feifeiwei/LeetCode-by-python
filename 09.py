
'''
判断一个整数是否是回文数。
'''
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            x = str(x)
            
            return x==x[::-1]
