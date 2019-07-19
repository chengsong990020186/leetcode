# 跳台阶
# Q: 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
# A: 斐波那契数列
# 假设第一次跳的是一阶，那么剩下的n-1个台阶，跳法是f(n-1)
# 假设第一次跳的是两阶，那么剩下的n-2个台阶，跳法是f(n-2)
# 由上面两种假设可得：f(n) = f(n-1) + f(n-2)
# 由实际情况可知：f(1) = 1，f(2) = 2
# 最终得出的是一个斐波那契数列

class Solution:
    def jumpFloor(self,n):
        if n>=0 and n<=2:
            return n
        while n>2:
            return Fibonacci(n-1)+Fibonacci(n-2)

Solution().jumpFloor(10)