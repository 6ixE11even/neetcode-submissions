class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # unique_set = set(nums)
        # if len(unique_set) < len(nums):
        #     return True
        # return False
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False