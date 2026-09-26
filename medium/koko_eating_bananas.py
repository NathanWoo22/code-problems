class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def calcTime(speed):
            time = 0
            for i, pile in enumerate(piles):
                time += math.ceil(pile / speed)

            return time 

        upper = max(piles)
        lower = 1
        workingSpeed = upper
        while upper >= lower: 
            speed = (upper + lower) // 2
            time = calcTime(speed)
            if time > h:
                lower = speed + 1 
            elif time <= h and speed > lower: 
                workingSpeed = speed
                upper = speed - 1 
            else:
                workingSpeed = speed
                break
        return workingSpeed
