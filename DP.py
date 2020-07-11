class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        solu_cnt = [0, 1, 2]

        for i in range(3, n + 1):
            solu_cnt.append(solu_cnt[i - 1] + solu_cnt[i - 2])

        return solu_cnt[n]