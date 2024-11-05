
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #快慢指针法
        slow=1
        fast=1
        while fast<len(nums):
            if nums[fast]!=nums[fast-1]: #fast和fast-1进行比较
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
            else:
                fast+=1
        return slow




