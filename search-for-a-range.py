# By Zehan Zhao <i@allenzhao.com>
# Blog : http://blog.allenzhao.com
# Blog post link: http://blog.allenzhao.com/leetcode/2014/09/15/LeetCode-Search-for-a-range/
# LeetCode Link: https://oj.leetcode.com/problems/search-for-a-range/
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        result = [-1, -1]
        if len(A)==0:
            return result
        # Search for left bound
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            result[0] = start
        elif A[end] == target:
            result[0] = end
        else:
            result = [-1, -1]
            return result

        start, end = 0, len(A) -1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[end] == target:
            result[1] = end
        elif A[start] == target:
            result[1] = start
        else:
            result = [-1, -1]
            return result

        return result
