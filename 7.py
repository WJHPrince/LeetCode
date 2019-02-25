class Solution:
    def reverse(self, x: 'int') -> 'int':
        temp = str(x)
        length = len(temp)
        lists = []
        new_list = []
        for i in range(0,length):
            lists.append(temp[i:i+1])
        if lists[0] == '-':
            new_list.append('-')
            for j in range(length-1):
                new_list.append(lists[-1-j])
        else:
            for k in range(length):
                new_list.append(lists[-1-k])
        new_str = ''.join(new_list)
        num = int(new_str)
        if num > 2**31-1:
            num = 0
        else:
            if num < -(2**31):
                num = 0
        return num
