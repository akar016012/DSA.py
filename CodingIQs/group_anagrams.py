# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def groupAnagrams(self, strs):
    res = {}
    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str not in res:
            res[sorted_str] = []
        res[sorted_str].append(s)
    return list(res.values())
