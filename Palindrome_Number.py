"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

# Solution 1 : By converting the integer to string
class Solution:
    def isPalindrome(self, x):

        if len(str(x)) == 1:
            return False

        if len(str(x)) == 2:
            if x % 10 == int(x/10):
                return True
            else:
                return False

        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

# Soltuion 2 : Without Converting the integer to string
    def palindromcheck(x):

        # Base Case

        if x >= 0 and x < 10:
            return True


        if x % 10 == int(x / 10):
            return True

        else:

            temp = x
            rev = 0

            while( x > 0 ):

                dig = x % 10

                rev = rev * 10 + dig
                x = x // 10

            if temp == rev:
                return True
            else:
                return False
