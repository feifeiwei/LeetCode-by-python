'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
	

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		
		a = nums[0]
		b = 0
		
		for s in nums:
			if b < 0:
				b = s
			else
				b += s
			a = max(a,b)
			
		return a
		
		
		
		
		
