print("water jug problrm")
#provides a default value for the dictionary keys if they don't exist.
from collections import defaultdict
jug1, jug2, aim = 4, 3, 2
visited = defaultdict(lambda: False)
def waterJugSolver(amt1, amt2):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True
    if visited[(amt1, amt2)] == False:
        print(amt1, amt2)
        visited[(amt1, amt2)] = True
                #Pouring all water from jug1 into jug2.
        return (waterJugSolver(0, amt2) or
                #Pouring all water from jug2 into jug1.
                waterJugSolver(amt1, 0) or
                #Filling jug1 to its maximum capacity.
                waterJugSolver(jug1, amt2) or
                #Filling jug2 to its maximum capacity.
                waterJugSolver(amt1, jug2) or
                #Pouring water from jug1 to jug2 until jug2 is full or jug1 is empty.
                waterJugSolver(amt1 + min(amt2, (jug1-amt1)), amt2 - min(amt2, (jug1-amt1))) or
                #Pouring water from jug2 to jug1 until jug1 is full or jug2 is empty.
                waterJugSolver(amt1 - min(amt1, (jug2-amt2)), amt2 + min(amt1, (jug2-amt2))))
    else:
        return False

print("Steps: ")

waterJugSolver(0, 0)