class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1=[]
        dict1={'(':')','[':']','{':'}'}
        for i in s:
            if i in dict1:
                list1.append(i)
            elif not list1 or dict1[list1.pop()]!=i:
                return False
        return not list1
    
Solution().isValid('({[]})')