# 2.替换空格
# Q: 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
# A: Python replace函数

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(' ','%20')

s='We Are Happy'
Solution().replaceSpace(s)