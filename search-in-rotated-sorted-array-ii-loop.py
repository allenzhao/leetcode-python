# Foor-loop version
# By Zehan Zhao <i@allenzhao.com>
# Blog : http://blog.allenzhao.com
# Blog post link: http://blog.allenzhao.com/leetcode/2014/09/17/LeetCode-Search-in-Rotated-Sorted-Array-II/
# LeetCode Link: https://oj.leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if not A:
            return False
        for ele in A:
            if target == ele:
                return True
        return False
