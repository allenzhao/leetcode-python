# By Zehan Zhao <i@allenzhao.com>
# Blog : http://blog.allenzhao.com
# Blog post link: http://blog.allenzhao.com/leetcode/2014/09/14/LeetCode-Search-Inser-Position/
# LeetCode Link: https://oj.leetcode.com/problems/search-insert-position/
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if not A:
            return -1
        if target < A[0]:
            return 0

        start, end = 0, len(A) - 1
        if A[end] < target:
            return end + 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            if A[mid] < target:
                start = mid
            if A[mid] > target:
                end = mid

        if A[start] == target:
            return start

        if A[end] == target:
            return end

        return start + 1

