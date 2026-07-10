class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # create a hashmap using nums (value -> index)
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for idx in range(len(nums)):
            complement = target - nums[idx]
            if complement in hashmap and idx != hashmap[complement]:
                return [idx, hashmap[complement]]
        
