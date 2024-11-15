from typing import List

#*******暴力解法*********（对于出界问题进行考虑）
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        if nums[0] > target:  # 判断临界位置
            return 0
        elif nums[len(nums) - 1] < target:
            return len(nums)

        while i <= j:
            mid =( i + j) // 2  # 修正 mid 的计算方式
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return i  # 如果没有找到，返回插入位置

#*****最优解
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        while i <= j:
            mid =( i + j) // 2  # 修正 mid 的计算方式
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return i  # 如果没有找到，返回插入位置