
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
#思路一：利用双指针，从后往前依次进行遍历比较
        i,j=len(s)-1,len(t)-1 #i,j对应的是字符串的下标，所以等于  ‘字符串长度-1’
        flag_s,flag_t=0,0 #用flag_s和_t依次记录s和t字符串中‘#’的个数
        while i>=0 or j>=0:
            while i>=0:
                if s[i]=='#' :
                    flag_s+=1
                    i=i-1
                elif s[i]!='#' and flag_s>0 :
                    flag_s-=1
                    i=i-1
                else: #表示s【i】此时代表为a到z之间的数
                    break
            while j>=0:
                if t[j]=='#' :
                    flag_t+=1 #
                    j=j-1
                elif t[j]!='#' and flag_t>0 :
                    flag_t-=1 #
                    j=j-1
                else: #表示s【i】此时代表为a到z之间的数
                    break
            if i>=0 and j>=0:
                if s[i]!=t[j]:
                    return False
            elif i>=0 or j>=0:
                return False
            i=i-1
            j=j-1 #####
        return True