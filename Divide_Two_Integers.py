"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
1. Both dividend and divisor will be 32-bit signed integers.
2. The divisor will never be 0.
3. Assume we are dealing with an environment which could only store integers
   within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
   this problem, assume that your function returns 231 − 1 when the division
   result overflows.
"""

class Solution:

    def divide(self, dividend, divisor):
        # Returns (greatest 2^i * divisor <= a, 2^i) or (0,0) if divident < divisor
        def helper(a, divisor):
            if dividend < divisor:
                return 0,0
            d = divisor
            next_d = d + d
            q = 1
            while next_d <= a:
                d = next_d
                next_d += next_d
                q += q
            return d, q

        negSign = (dividend>0) ^ (divisor>0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        d, q = helper(dividend, divisor)
        while dividend - d >= divisor:
            dd, qd = helper(dividend - d, divisor)
            d += dd
            q += qd
        return min(2147483647, (-1 if negSign else 1) * q)
