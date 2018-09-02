"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution:
    def longestCommonPrefix(self, strs):

        if len(strs) == 0 or len(strs[0]) == 0:
            return ""
        letter = strs[0][0]
        dic = {letter: ""}
        letterArray = []
        for word in strs:
            if len(word) == 0:
                return ""
            if word[0] not in dic:
                return ""
            else:
                letterArray.append(word[1:])
        return letter + self.longestCommonPrefix(letterArray)
