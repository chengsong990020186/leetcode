# 调整数组顺序使奇数位于偶数前面
# Q: 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

# A: 函数的扩展功能。把函数中的判断条件拿出来，写成一个函数。奇数位于偶数前面的情况，类似于快排，头尾各设置一个指针，头指针为奇数则后移，尾指针为偶数则前移。但是快排不稳定，会打破相对位置。所以用python可以一行搞定： lambda大法。

class Solution:
    def reOrderArray(self, array):
        # write code here
        return sorted(array,key=lambda c:c%2,reverse=True)