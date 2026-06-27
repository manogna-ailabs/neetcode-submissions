class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'
        deadends = set(deadends)
        if target in deadends or start in deadends:
            return -1
        
        visited = set()
        q = deque([start])
        visited.add(start)
        turns = 0

        def get_neighbours(state):
            neighbours = []
            for k in range(4):
                num = int(state[k])
                up, down = (num + 1) % 10, (num - 1) % 10
                neighbours.append(state[:k] + str(up) + state[k+1:])
                neighbours.append(state[:k] + str(down) + state[k+1:])
            return neighbours

        while q:
            for i in range(len(q)):
                state = q.popleft()
                if state == target:
                    return turns
                nn = get_neighbours(state)
                for n_state in nn:
                    if n_state not in visited and n_state not in deadends:
                        visited.add(n_state)
                        q.append(n_state)

            turns += 1

        return -1