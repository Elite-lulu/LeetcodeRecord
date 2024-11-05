from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #左区间进行二分查找
        #条件：查找到target坐标的值为0或者他左边一个数值比它本身小，那么这个位置可以记作为target起始位置
        def search_left(nums:List[int], target:int) -> int:
            i,j=0,len(nums)-1
            while i<=j:
                mid=(i+j)//2
                if nums[mid]==target:
                    if mid==0 or nums[mid]>nums[mid-1]:
                        return mid
                    else:
                        j=mid-1
                elif nums[mid]>target:
                    j=mid-1
                else:
                    i=mid+1
            return -1
        # 右区间进行二分查找
        # 条件：查找到target坐标的值为len[nums]-1 或者 他右边一个数值比它本身大，那么这个位置可以记作为target结束位置
        def search_right(nums:List[int], target:int) -> int:
            i,j=0,len(nums)-1
            while i<=j:
                mid=(i+j)//2
                if nums[mid]==target:
                    if mid==len(nums)-1 or nums[mid]<nums[mid+1]:
                        return mid
                    else:
                        i=mid+1
                elif nums[mid]>target:
                    j=mid-1
                else:
                    i=mid+1
            return -1

        return [search_left(nums,target),search_right(nums,target)]