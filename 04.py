'''
两个排序数组的中位数
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5

'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = j = 0
        ret = []
        total_len = len(nums1)+len(nums2)
        
        for k in range(total_len):
            if i > len(nums1)-1:
                ret.append(nums2[j])
                j+=1
            elif j > len(nums2)-1:
                ret.append(nums1[i])
                i += 1
            elif nums1[i]<nums2[j]:
                ret.append(nums1[i])
                i += 1
            else:
                ret.append(nums2[j])
                j += 1
        print(ret)
        if total_len % 2 == 0:
            return (ret[total_len//2] + ret[total_len//2 - 1])/2.
        else:
            return ret[total_len//2]
