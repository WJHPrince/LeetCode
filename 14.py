class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        length = len(strs)
        position = 0
        if "" in strs:
            return ""
        else:
            if length == 0:
                return ""
            else:
                if length == 1:
                    return strs[0]
                else:
                    short = len(str(strs[0]))
                    for i in range(1,length):
                        if len(strs[i]) < short:
                            short = len(strs[i])
                            position = i
                    for num in range(1,short+1):
                        for temp in strs:
                            if temp[0:num] == strs[position][0:num]:
                                flag = 1
                            else:
                                flag = 0
                            if flag == 0:
                                break
                        if flag == 0:
                            return strs[position][0:num-1]
                            break
                    if flag == 1 and num == short:
                        return strs[position]
