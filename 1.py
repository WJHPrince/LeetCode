class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        for fir_num in range(0,len(nums)):
            for sec_num in range(fir_num+1,len(nums)):
                test = nums[fir_num] + nums[sec_num]
                if test == target:
                    return fir_num,sec_num
