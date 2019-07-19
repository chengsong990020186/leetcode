# 斐波那契数列
# Q: 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
# A: 1.不使用递归实现数列，需要把前面两个数字存入在一个数组中,实际一直在更新。
#    2.使用递归

class Solution:
    def Fibonacci(self,n):
        tempArray = [0,1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
                print(tempArray)
        return tempArray[n%2]

class Solution:
    def Fibonacci(self,n):
        if n>=0 and n<=2:
            return n
        while n>2:
            return Fibonacci(n-1)+Fibonacci(n-2)
    
Solution().Fibonacci(10)