class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_to_target = {}
        fleets = []
        for p, s in zip(position, speed):
            time_to_target[p] = (target-p)/s
        time_to_target = {k:v for k,v in sorted(time_to_target.items(), reverse=True)}
        for p, t in time_to_target.items():
            if not fleets or t > fleets[-1]:
                fleets.append(t)
        return len(fleets)