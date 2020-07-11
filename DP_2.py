class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        result_arr = [0, 1, 2, 3, 1]

        for i in range(5, n + 1):
            result_arr.append(1000)

            j = 1
            while i - j * j >= 0:
                result_arr[i] = min(result_arr[i], result_arr[i - j * j] + 1)
                j += 1

        return result_arr[n]