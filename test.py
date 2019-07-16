class Solution(object):
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            if (target - num) in h:
                return [i, h[target - num]]
            h[num] = i
