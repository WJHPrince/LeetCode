class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sums = 0
        length = len(s)
        for num in range(0, length - 1):
            if maps[s[num:num+1]] < maps[s[num+1:num+2]]:
                sums = sums - maps[s[num:num+1]]
            else:
                sums = sums + maps[s[num:num+1]]
        sums = sums + maps[s[-1]]
        return sums
