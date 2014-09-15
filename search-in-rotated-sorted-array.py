# By Zehan Zhao <i@allenzhao.com>
# Blog : http://blog.allenzhao.com
# Blog post link: http://blog.allenzhao.com/leetcode/2014/09/16/LeetCode-Search-in-Rotated-Sorted-Array
# LeetCode Link: https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if not A:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            if A[mid] > A[start]:
                if A[start] <= target and A[mid] > target:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] < target and A[end] >= target:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
