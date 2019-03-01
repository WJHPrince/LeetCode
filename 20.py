class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        dirc = {"(":")","{":"}","[":"]"}
        left = ['(','[','{']
        stack = []
        if length % 2 == 1:
            return False
        else:
            for num in range(0,length):
                if s[num] in left:
                    stack.append(dirc[s[num]])
                if s[num] not in left:
                    if stack == [] or stack[-1] != s[num]:
                        return False
                    else:
                        stack.pop(-1)
            if stack == []:
                return True
            else:
                return False
# 这个是我看了答案后自己重新写的类似堆栈操作的方案，其实还能再省略一点，空一点内存空间出来（但是我懒得改了.lazy）
