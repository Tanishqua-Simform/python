# 17. Letter Combinations of a Phone Number
## Not a part of Leetcode Blind 75
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

def letterCombinations(digits: str) -> list:
    if not digits:
        return []
    n = len(digits)
    phone_mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    combinations = []
    stack = []

    def backtrack(i):
        if i == n:
            msg = ''.join(stack)
            combinations.append(msg)
            return 
        
        for ch in phone_mapping[digits[i]]:
            stack.append(ch)
            backtrack(i + 1)
            stack.pop()
        return 
    backtrack(0)
    return combinations