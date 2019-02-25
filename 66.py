class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        digits[-1] = digits[-1] + 1
        flag = 0
        for i in range(0,len(digits)):
            if digits[i] > 9:
                flag = flag + 1
        while flag != 0:
            for num in range(-len(digits),0):
                if digits[num] > 9:
                    digits[num] = digits[num] - 10
                    if num == -len(digits):
                        digits.insert(0,1)
                    else:
                        digits[num-1] = digits[num-1] + 1
                    flag = flag - 1
                    for j in range(-len(digits),0):
                        if digits[j] > 9:
                            flag = flag + 1
        return digits
