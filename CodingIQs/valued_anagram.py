# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(self, s, t):
    # optimized space O(1)
    return sorted(s) == sorted(t)

    # optimized
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True

    # using hashmap

    if len(s) != len(t):
        return False

    hashS, hashT = {}, {}

    for i in range(len(s)):
        hashS[s[i]] = 1+hashS.get(s[i], 0)
        hashT[t[i]] = 1+hashT.get(s[i], 0)
    for c in hashS:
        if hashS[c] != hashT.get([c], 0):
            return False
    return True
