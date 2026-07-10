class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # create a hashmap using nums (value -> index)
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        #  loop through nums
        for idx in range(len(nums)):

            # calculate complement
            complement = target - nums[idx]

            # 1st condition: whether complement exists in hashmap
            # 2nd condition: idx must not be equal to hashmap[complement]

            # for eg. [3,4,5,6] and target is 6
            # without 2nd condition, complement = 6 - 3 = 3 which exist in list
            # so it is using same number (at same idx) twice
            if complement in hashmap and idx != hashmap[complement]:
                return [idx, hashmap[complement]]
        
