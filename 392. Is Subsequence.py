# Key Takeaway:
# When tracing 2 lists, what should you do?
# You should use 2 pointers to track their status.
# Especially when the return value is a Boolean. 
# And it requires you to consider traverse speed differences.

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 
# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = []
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if t[j] is not s[i]:
                j += 1
            else:
                i += 1
                j += 1
        if i >= len(s):
            return True
        else:
            return False

 
