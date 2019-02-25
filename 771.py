class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        temp = 0
        for i in range(0,len(J)):
            for j in range(0,len(S)):
                if S[j:j+1] == J[i:i+1] :
                    temp = temp + 1
        return temp
