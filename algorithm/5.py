# -*- coding: utf-8 -*-
"""
5. Longest Palindromic Substring
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        sl = ""

        for i in xrange(0, n):
            for j in xrange(i + 1, n + 1):
                substr = s[i:j]
                if self.isPalindrome(substr) and (len(substr) > len(sl)):
                    sl = substr

        return sl

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return str(s) == str(s)[::-1]


def main():
    solution = Solution()
    print solution.longestPalindrome('babad')


if __name__ == "__main__":
    main()
