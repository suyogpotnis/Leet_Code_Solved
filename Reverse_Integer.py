"""
Given a 32-bit signed integer, reverse digits of an integer.

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers
 within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
 of this problem, assume that your function returns 0 when the reversed integer overflows.
 
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Edge Case Checks
        if x == 0:
            return 0

        if x == 1 :
            return 1

        # Defining Multiplier to handle negative values
        multiplier = 1
        if x >= 1:
            multiplier = 1
        else:
            multiplier = -1

        # Convert Negative to Positive
        if "-" in str(x):
            x = x * -1
        else:
            x = x

        a = x
        b = x

        returnvalue = ''

        while int(b / 10) > 0:
            a = b % 10
            returnvalue = str(returnvalue) + str(a)
            b = int(b / 10)

        returnvalue = int(returnvalue+str(x)[0])* multiplier

        if int(returnvalue) > 2**31 or int(returnvalue) < -2**31:
            return 0
        else:
            return returnvalue
