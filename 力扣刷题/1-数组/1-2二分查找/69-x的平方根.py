
#思路： 利用二分查找，在数组1到x区间内，进行手算模拟，尤其注意最终返回为return j
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        i,j=1,x
        while i<=j:
            mid=i+(j-i)//2
            if mid**2==x:
                return mid
            elif mid **2 >x:
                j=mid-1
            else:
                i=mid+1
        return j