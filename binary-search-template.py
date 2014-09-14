# By Zehan Zhao <i@allenzhao.com>
# Blog : http://blog.allenzhao.com
# Blog post link: http://blog.allenzhao.com/lintcode/2014/09/13/Template-for-Binary-search/
# LintCode Link: http://lintcode.com/en/problem/binary-search/

class Solution:
    # @param array the array
    # @param target target to search
    # @return the first position of target
    def binarySearch(self, array, target):
        if not array:
            return -1

        start, end = 0, len(array) - 1

        while start + 1 < end:
            mid = start + (start + end) / 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                start = mid
            elif array[mid] > target:
                end = mid

        if array[start] == target:
            return start
        if array[end] == target:
            return end

        return -1
