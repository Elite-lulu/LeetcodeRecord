from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #思路：利用快慢指针，对于不等于0的元素赋给慢指针。若遇到等于0的元素则用add累加，最后把0依次插入到nums末尾
        add=0 #add用于记录原数组中0的个数
        slow,fast=0,0
        while fast<len(nums): #
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
            elif nums[fast]==0:
                fast+=1
                add=add+1
        while add>0:
            nums[slow]=0
            slow+=1
            add-=1
        return nums #
