class Solution:
    """
    @param matrix,i a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        end = rows * cols - 1;
        while start + 1 < end:
            mid = start + (end - start) / 2
            current = matrix[mid / cols][mid % cols]
            if current == target:
                return True
            elif current < target:
                start = mid
            else:
                end = mid

        if matrix[start / cols][start % cols] == target:
            return True
        if matrix[end / cols][end % cols] == target:
            return True
        return False
