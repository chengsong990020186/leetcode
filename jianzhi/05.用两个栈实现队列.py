# 用两个栈实现队列
# Q: 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

# A: 两个栈stack1和stack2， push的时候直接push进stack1，pop时需要判断stack1和stack2中的情况。如果stack2不为空的话，直接从stack2中pop，如果stack2为空，把stack1中的值push到stack2中，然后再pop stack2中的值。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, node):
        # write code here
        self.stack1.append(node)
        
    def pop(self):
        # return xx
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return 
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
           
        return self.stack2.pop()