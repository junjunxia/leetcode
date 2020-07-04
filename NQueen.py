class Solution(object):
    solution_count = 0

    def check(self, row, column, array, N):
        for i in range(row):
            if array[i][column] == 1:
                return False
        for j in range(column):
            if array[row][j] == 1:
                return False

        i = row - 1
        j = column - 1
        while i >= 0 and j >= 0:
            if array[i][j] == 1:
                return False

            i = i - 1
            j = j - 1

        i = row + 1
        j = column -1

        while i < N and j >= 0:
            if array[i][j] == 1:
                return False
            i = i + 1
            j = j - 1


        return True

    def findNQueens(self, current_index, N, array):
        if current_index >= N:
            self.solution_count += 1

        else:
            for k in range(N):
                if self.check(k, current_index, array, N):
                    array[k][current_index] = 1
                    self.findNQueens(current_index + 1, N, array)
                    array[k][current_index] = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        array = [[0] * n for i in range(n)]
        self.findNQueens(0, n, array)
        return self.solution_count

s = Solution()
print (s.totalNQueens(8))






