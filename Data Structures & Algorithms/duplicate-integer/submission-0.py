class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = set(nums)
        if len(new_list) == len(nums):
            return False
        else:
            return True
        