# 20.有效的括号
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:

# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -2**31+1
        cursum = 0
        for num in nums:
            cursum = max(cursum+num,num)
            res = max(res,cursum)
        return res

Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])



