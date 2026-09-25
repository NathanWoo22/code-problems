class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        comp = []
        for i, val in enumerate(position):
            comp.append([val, speed[i]])
        
        comp = sorted(comp)[::-1]
        stack = []
        fleets = 0
        for i, car in enumerate(comp):
            if len(stack) == 0:
                stack.append([car, (target - car[0]) / car[1]])
            
            else: 
                if (target - car[0]) / car[1] <= stack[-1][1]:
                    stack.append([car, max((target - car[0]) / car[1], stack[-1][1])])
                else: 
                    stack = []
                    fleets += 1
                    stack.append([car, (target - car[0]) / car[1]])
                
        if len(stack) != 0:
            fleets += 1
        
        return fleets
