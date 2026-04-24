class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = dict()
        distances = []
        for point in points:
            d = point[0]**2 + point[1]**2
            dist[d] = dist.get(d, []) + [point]
            distances += [-d]

        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)

        out = []
        seen_distances = set()
        for i in range(len(distances)):
            d_val = -distances[i]
            if d_val not in seen_distances:
                for point in dist[d_val]:
                    if len(out) < k:
                        out.append(point)
                seen_distances.add(d_val)
        return out