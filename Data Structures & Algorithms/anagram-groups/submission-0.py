class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        if len(strs) == 0:
            output.append([""])
            return output

        if len(strs) == 1:
            output.append(strs)
            return output

        # Sorting Method
        # each anagram after sorting returns same signature
        # eg. "act" and "cat" both becomes "act" after sorting
        # eg. "stop", "pots", "tops" all become "opst" after sorting
        # we will check if the signature exists in a hashmap, if not add it as a key and word as value
        # we will return list of dict.values as final output

        hashmap = {}
        key_list = []


        for word in strs:

            if tuple(sorted(word)) not in hashmap:
                key_list = []
                key_list.append(word)
                hashmap[tuple(sorted(word))] = key_list
            else:
                hashmap.get(tuple(sorted(word))).append(word)
                # hashmap[tuple(sorted(word))] = key_list

        return list(hashmap.values())