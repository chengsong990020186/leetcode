# 旋转数组的最小数字
# Q: 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# A: 二分查找的变形，旋转数组的首元素肯定不小于旋转数组的尾元素，找一个中间点，如果中间点比首元素大，说明最小数字在中间点后面，如果中间点比尾元素小，说明最小数字在中间点前面。然后循环。 但是在一次循环中，首元素小于尾元素，说明该数组是排序的，首元素就是最小数字，如果出现首元素、尾元素、中间值三者相等，则只能在此区域中顺序查找。

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        front = 0
        rear = len(rotateArray) - 1
        minVal = rotateArray[0]
        
        if rotateArray[front] < rotateArray[rear]:
            return rotateArray[front]
        else:
            while (rear - front) > 1: 
                mid = (front + rear) // 2
                if rotateArray[mid] >= rotateArray[front]:
                    front = mid
                elif rotateArray[mid] <= rotateArray[rear]:
                    rear = mid
                elif rotateArray[front] == rotateArray[rear] == rotateArray[mid]:
                    for i in range(1, len(rotateArray)):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                            rear = i
            minVal = rotateArray[rear]
            return minVal

