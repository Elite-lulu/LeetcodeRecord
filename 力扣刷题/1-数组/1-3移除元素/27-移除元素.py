
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #暴力算法，依次前移
        i,j=0,len(nums) #此时的j代表数组内元素的个数，不代表下标值！

        while i<j:
            if nums[i]!=val:

                i=i+1
            elif nums[i]==val:#当出现要移除的元素时
                for k in range (i+1,j): #执行前移 注意！！！！：range函数是个左闭右开的函数！！
                    nums[k-1]=nums[k]
                j=j-1
        return j #用 j+1 代表数组中此时的元素个数

    def removeElement2(self, nums: List[int], val: int) -> int:
        #方法：快慢指针
        #思路：快指针：寻找新数组的元素 ，新数组就是不含有目标元素的数组，利用快指针的依次遍历，并赋值给慢指针，从而实现了双指针法
        #     慢指针：代表新数组下标的位置
        slowIndex=0 #慢指针
        fastIndex=0 #快指针
        while fastIndex<len(nums):
            if nums[fastIndex]!=val: #遇到
                nums[slowIndex]=nums[fastIndex]
                slowIndex=slowIndex+1
            else:
                fastIndex=fastIndex+1
        return slowIndex
