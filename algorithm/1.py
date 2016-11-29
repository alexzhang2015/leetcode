# -*- coding: utf-8 -*-
"""
1. Two Sum
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return str([i, j])


def main():
    solution = Solution()
    print solution.twoSum([2, 7, 11, 15], 18)

if __name__ == "__main__":
    main()
