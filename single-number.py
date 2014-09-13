# By Zehan Zhao <i@allenzhao.com>
# Blog : http://blog.allenzhao.com
# Blog post link: http://blog.allenzhao.com/leetcode/2014/09/13/leetcode---single-number/
# LeetCode Link: https://oj.leetcode.com/problems/single-number/
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
            result ^= i
        return result
