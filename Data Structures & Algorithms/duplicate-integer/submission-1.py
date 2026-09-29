class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     if nums.count(nums[i]) >1:
        #         return True
        # return False
        uniq=set(nums)
        if len(nums) == len(uniq): 
            return False
        else:
            return True