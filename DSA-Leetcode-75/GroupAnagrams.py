# 49. Group Anagrams
## Not a part of Leetcode Blind 75
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
'''
from collections import defaultdict
def groupAnagrams(strs: list) -> list:
    anagrams = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return [group for group in anagrams.values()]