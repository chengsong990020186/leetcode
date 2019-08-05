# 二进制中1的个数
# Q: 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

# A: 每个非零整数n和n-1进行按位与运算，整数n的二进制中，最右边的1就会变成0，利用循环，计算经过几次运算二进制变成0，就有几个1。

class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            count += 1
            n = (n - 1) & n
        return count
