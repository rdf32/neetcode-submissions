class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted([(pos, spd) for pos, spd in zip(position, speed)], reverse=True)
        times = [(target - pos) / spd for pos, spd in cars]


        fleets    = 0
        last_time = 0

        for time in times:
            if time > last_time:
                fleets += 1
                last_time = time

        return fleets        