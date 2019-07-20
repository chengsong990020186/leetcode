# 3.从尾到头打印链表
# Q: 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
# A: 从头到尾遍历链表，并用一个栈存储每个节点的值，之后出栈输出，用insert()，一直在index=0的位置插入遍历的值。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        
        result =[]
        
        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode.next
        return result