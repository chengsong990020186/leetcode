# 二维数组中的查找
# Q: 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# A: 从左上或者右下开始查找。从右上开始查找：如果数组中的数比这个整数大，向左移动一位，如果数组中的数比这个数小，向下移动一位。

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array == []:
            return False
        num_row = len(array)
        num_col = len(array[0])
        
        i = num_col - 1
        j = 0
        
        while i >= 0 and j < num_row:
            if array[j][i] > target:
                i -= 1
            elif array[j][i] < target:
                j += 1
            else:
                return True

array=np.array(range(1,101)).reshape(10,10).tolist()
Solution().Find(88,array)