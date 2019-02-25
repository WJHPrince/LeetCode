class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        length = len(temp)
        flag = 0
        for i in range(0,length):
            if temp[i:i+1] != temp[length-1-i:length-i]:
                flag = 1
        if flag == 1:
            return False
        else:
            return True

