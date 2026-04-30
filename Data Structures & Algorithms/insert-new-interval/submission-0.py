class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        out = [intervals[0]]
        for i in range(1, len(intervals)):
            i1 = out[-1]
            i2 = intervals[i]
            if i2[0] <= i1[1]:
                out.pop()
                out.append([i1[0], max(i1[1], i2[1])])
            else:
                out.append(i2)
        return out

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        heapq.heapify(intervals)
        heapq.heappush(intervals, newInterval)
        return self.merge(intervals)