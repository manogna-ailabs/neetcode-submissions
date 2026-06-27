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

        def add_neighbours(state):
            for k in range(4):
                num = int(state[k])
                up, down = (num + 1) % 10, (num - 1) % 10
                n_state = state[:k] + str(up) + state[k+1:]
                if n_state not in visited and n_state not in deadends:
                    visited.add(n_state)
                    q.append(n_state)
                n_state = state[:k] + str(down) + state[k+1:]
                if n_state not in visited and n_state not in deadends:
                    visited.add(n_state)
                    q.append(n_state)

        while q:
            for i in range(len(q)):
                state = q.popleft()
                if state == target:
                    return turns
                add_neighbours(state)
            turns += 1

        return -1