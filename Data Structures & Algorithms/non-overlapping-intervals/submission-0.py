class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0])
        n = len(intervals)

        def dfs(i, prev):
            if i == n:
                return 0
            res = dfs(i + 1, prev)
            if prev == -1 or intervals[prev][1] <= intervals[i][0]:
                res = max(res, 1 + dfs(i + 1, i))
            return res
        kept = dfs(0, -1)
        return n - kept
