# 矩形覆盖
# Q: 我们可以用2 1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 1的小矩形无重叠地覆盖一个2 * n的大矩形，总共有多少种方法？
# A: 依然是斐波那契数列的变形。代码参考跳台阶。

class Solution:
    def rectCover(self,n):
        if n>=0 and n<=2:
            return n
        while n>2:
            return rectCover(n-1)+rectCover(n-2)

Solution().rectCover(10)
