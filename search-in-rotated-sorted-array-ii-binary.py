# Binary search version
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
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return True
            if A[mid] > A[start]:
                if A[start] <= target and A[mid] > target:
                    end = mid
                else:
                    start = mid
            elif A[mid] < A[start]:
                if A[mid] < target and A[end] >= target:
                    start = mid
                else:
                    end = mid
            else:
                start += 1

        if A[start] == target:
            return True
        if A[end] == target:
            return True
        return False
