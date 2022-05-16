jugs = []
numberOfJugs = 2
# just makes a jug object with capacity and current state
class Jug():
    def __init__(self, capacity, state):
        self.capacity = capacity
        self.state = state
#returns the jug with the bigger capcity first
def lengths(jug1, jug2):
    if jug2.capacity >= jug1.capacity:
        return jug2, jug1
    else:
        return jug1, jug2

def swapMethod(x,y, lMaxi, sMaxi):
    print("given: ", x, y)
    #input:(0, y) output: (lMaxi, y)
    if x == 0:
        print("added")
        return lMaxi, y
    
    # output: (x, min)
    elif y == 0:
        print("else ", x, sMaxi)
        return x,sMaxi
    # if y == 0:    
    elif y == sMaxi:
        print("x: ",x, "y: ", y,)
        return x,0    
    
    #Input:(lMaxi, y) output:(0, y)
    elif x == lMaxi:
        print(0,y)
        return 0,y

#Has to detect if going horizontally up or down
def totalMethod(x,y, lMaxi, sMaxi):  
    #Going horizontally down
    if x == 0 or y == sMaxi:
        return min(lMaxi, (x+y)), max((x+y-lMaxi), 0)
    #Going horizontally up
    else:
        return max((x+y-sMaxi), 0), min(sMaxi, (x+y))   



def pingPong(jugs, targetCapacity):
    jug1,jug2 = lengths(jugs[0], jugs[1]) #sees which jug is bigger
    lMaxi, sMaxi = jug1.capacity, jug2.capacity
    x,y = jug1.state, jug2.state# This puts the water in the starting jugs
    
    history = f'''
_____{lMaxi}___{sMaxi}_|
01 | {x} | {y} |'''
    x,y = totalMethod(x,y, lMaxi, sMaxi) #always start with the total method
    past = 0
    history += f'''
02 | {x} | {y} |\n'''
    for i in range(0,1000):
        if x == targetCapacity or y == targetCapacity:
            print(history)
            return history
        elif past == 0: #i mained the total method id = 0
            x,y = swapMethod(x,y,lMaxi,sMaxi)
            past = 1
        else:
            x,y = totalMethod(x,y, lMaxi, sMaxi)
            past = 0
        history += f'{i+3:02} | {x} | {y} |\n'


def questions():
    try:
        for i in range(0,int(numberOfJugs)):
            capacity = max(0, int(input(f"Enter a postive integar for the capacity for jug {i}: ")))
            state = max(0, int(input(f"Enter a postive integar for the amount of water in jug {i}: ")))
            jugs.append(Jug(capacity, state))
        targetCapacity = max(0, int(input("Enter a postive target capacity: ")))
    except (ValueError):
        print("Make sure to input in a postive integar!!!")
        exit()
    pingPong(jugs, targetCapacity)

if __name__ == "__main__":
    questions()





