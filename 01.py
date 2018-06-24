'''
两数之和：

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

def solution(nums, target):
    
    D = {}
    
    for idx, num in nums:
        if num in D:
            return [idx, D[num]]
        else:
             D[target-num] = idx
    
    
    
    
