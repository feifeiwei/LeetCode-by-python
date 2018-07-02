'''
打家劫舍
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
[1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
'''
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0,0
        
        for s in nums:
            last, now = now, max(now, last+s)
        return now
        
