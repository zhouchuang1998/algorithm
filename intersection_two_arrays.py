# -*- coding: utf-8 -*-

""" 
    给定两个数组，编写一个函数来计算它们的交集。

    示例 1:

    输入: nums1 = [1,2,2,1], nums2 = [2,2]
    输出: [2]
    示例 2:

    输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出: [9,4]
    说明:

    输出结果中的每个元素一定是唯一的。
    我们可以不考虑输出结果的顺序。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # end = set()
        # dit = set()
        # for i in nums1:
        #     dit.add(i)
        # for j in nums2:
        #     if j in dit:
        #         end.add(j)

        # return list(end)
        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    s = Solution()
    a = s.intersection(nums1, nums2)
    print(a)
