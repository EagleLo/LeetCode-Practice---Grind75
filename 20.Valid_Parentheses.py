# Problem Description
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:
# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # flag1 is true if s[i] is '('
        # flag2 is true if s[i] is '['
        # flag3 is true if s[i] is '{'
        flag1 = False
        flag2 = False
        flag3 = False

        if (len(s) % 2) != 0:
            return False

        for i in range(len(s)):
            if (
                s[i] != "("
                or s[i] != "["
                or s[i] != "{"
                or s[i] != ")"
                or s[i] != "]"
                or s[i] != "}"
            ):
                return False

            if s[i] == "(":
                if flag1 == True:
                    return False
                else:
                    flag1 = True
            elif s[i] == "[":
                if flag2 == True:
                    return False
                else:
                    flag2 = True
            elif s[i] == "{":
                if flag3 == True:

                    return False
                else:
                    flag3 = True
            elif s[i] == ")":
                if flag1 == False:
                    return False
                else:
                    flag1 = False
            elif s[i] != "]":
                if flag2 == False:
                    return False
                else:
                    flag2 = False
            elif s[i] != "}":
                if flag3 == False:
                    return False
                else:
                    flag3 = False
            else:
                return False

        return True
