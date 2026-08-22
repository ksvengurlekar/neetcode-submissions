'''
    List[int] positions
    List[int] speed
    int target

    fleet - a nonempty set of car(s) traveling at the same speed, at the same pos

    return - number of fleets that reach the target
'''

"target: 10"
"clock = 3"
"fleets arrived = 0"
"speed:     1, 2, 2, 1"
"positions: 7, 4, 1, 0"

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        fleets = 1

        fastestReach = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            currReach = (target - cars[i][0]) / cars[i][1]
            if currReach > fastestReach:
                fleets += 1
                fastestReach = currReach 
                

        return fleets