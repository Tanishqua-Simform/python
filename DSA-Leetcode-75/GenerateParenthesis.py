# 22. Generate Parentheses
## Not a part of Leetcode Blind 75
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

def generateParenthesis(n: int) -> list:
    parenthesis = []

    def backtrack(curr, open_p, close_p):
        if open_p == close_p == n:
            parenthesis.append(curr)
            return
        if open_p < n:
            curr += '('
            backtrack(curr, open_p + 1, close_p)
            curr = curr[:-1]
        if close_p < open_p:
            curr += ')'
            backtrack(curr, open_p, close_p + 1)
            curr = curr[:-1]
        return 
    backtrack('', 0, 0)
    return parenthesis