class Solution(object):
    solution_list = []

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
            result_str_arr = []

            for row in array:
                result_row_result_str_arr = []
                for item in row:
                    if item == 0:
                        result_row_result_str_arr.append('.')
                    else:
                        result_row_result_str_arr.append('Q')
                result_str_arr.append(''.join(result_row_result_str_arr))

            self.solution_list.append(result_str_arr)

        else:
            for k in range(N):
                if self.check(k, current_index, array, N):
                    array[k][current_index] = 1
                    self.findNQueens(current_index + 1, N, array)
                    array[k][current_index] = 0

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.solution_list = []
        array = [[0] * n for i in range(n)]
        self.findNQueens(0, n, array)
        return self.solution_list

s = Solution()
print (s.solveNQueens(4))






