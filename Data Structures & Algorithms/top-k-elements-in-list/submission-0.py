from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        return sorted(hashmap, key=lambda x: hashmap[x], reverse=True)[:k]