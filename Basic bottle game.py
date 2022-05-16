jugs = []
numberOfJugs = 2


def swapMethod(x,y, tLength, sLength):   
    #input:(0, y) output: (tLength, y)
    if x == 0:
        print("added")
        return tLength, y
    
    #input: (x, 0) output: (x, min)
    elif y == 0:
        print("else ", x, sLength)
        return x,sLength

    #input: (x, sLength) output: (x, 0)    
    elif y == sLength:
        print("x: ",x, "y: ", y,)
        return x,0    

    #Input:(tLength, y) output:(0, y)
    elif x == tLength:
        print(0,y)
        return 0,y

#Has to detect if going horizontally up or down
def totalMethod(x,y, tLength, sLength):  
    #Going horizontally down
    if x == 0 or y == 5:
        return min(tLength, (x+y)), max((x+y-tLength), 0)
    #Going horizontally up
    else:
        return max((x+y-sLength), 0), min(sLength, (x+y))   



targetCapacity = 6 # Change this
tLength, sLength = 7,5 #Change this
x,y = 0,5 # Change this
history = f'''
_____{tLength}___{sLength}_|
01 | {x} | {y} |
'''
# First time one will always be the Total method
x,y = totalMethod(x,y, tLength, sLength)
past = 0
history += f'02 | {x} | {y} |\n'
for i in range(0,10):
    if x == targetCapacity or y == targetCapacity:
        break
    if past == 0: #i mained the total method id = 0
        x,y = swapMethod(x,y,tLength,sLength)
        past = 1
    else:
        x,y = totalMethod(x,y, tLength, sLength)
        past = 0
    history += f'{i+3:02} | {x} | {y} |\n'
    
print(history)