class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':
        temp_int = nums.count(val)
        for i in range(0, temp_int):
            nums.remove(val)
