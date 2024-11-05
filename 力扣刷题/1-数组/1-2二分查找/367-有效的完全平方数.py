

#思路：同力扣69题，用二分法找x的平方根
class Solution:
    def mySqrt(self, num: int) -> int:
        if num<1:
            return False
        if num==1:
            return True
        i,j=1,num
        while i<=j:
            mid=i+(j-i)//2
            if mid**2==num:
                return True
            elif mid **2 >num:
                j=mid-1
            else:
                i=mid+1
        return False
