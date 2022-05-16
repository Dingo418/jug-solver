Everyone knows the classic water jug problem. You are by a stream with a 5-Litre and a 7-Litre bucket. How do you measure out 6-Liters in the fewest possible pourings? You first fill up the 7 and so on.


![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1652416377767/9n608jHlA.png align="left")



You might not have seen this particular problem but you have definitely heard of a problem like this. But what many people do not know about this problem is you can actually solve it using the points of a Parallelogram or what some people call a pool table. If you translate your starting amount of water as 5 litres in the 5-litre jug, then you can translate it to (0,5). You can keep it bouncing off the points until you desired amount in the x or y. The parallelogram does the exact same thing as what we just did in the table above.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1652660739006/UtovqNSvf.png align="left")

I found that it was easier to find the patterns if I made the parallelogram a rectangle. There are 4 different variables you need to use this. The current x and y, the method you are using and the side & top length.  Once you have those 4 variables you can make any table. I strongly recommend following each line with your finger as I tell you the rules:

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1652660332517/5UsjUKUWH.png align="left")

### Phesudocode 
#### The Total Method:
The Total Method is when you add up the x and y and then flip it to the other side of the rectangle. If you look at the start point of the line and the endpoint of the line then the x+y will equal the same. There are 2 rules in the total method
1. if the red line is going horizontally down, then return the number that is minimum of (top length or x+y) and they as the maximum number that is either ((x+y- top length) or 0).
##### **How does rule 1 work?**
Count until you reach x+y from the bottom left to the bottom right and go up the right line if you reach it.
2.  If the red line is going horizontally up then return x as the maximum of either ((x+y)- side length or 0) and the y as the minimum of either (side length or (x+y).
##### **How does rule 2 work?**
Count until you reach x+y from the bottom left to the top of the left line and go up the right line until you reach it.

#### The Swap Method:
The swap method swaps the x or y depending on which line it is on. The swap method is made up of 4 smaller rules that each change specific variables in the coordinates depending on which side of the rectangle you are using the swap method on.
1. if x = 0 then return the top length and y
This is done as we need to flip 0,2 to
2. if y = 0 then return x with side length
3. if y = the side length then return x and 0
4. if x = the top length then return 0 and y

#### Extra rules:
We can also find out that to start the bouncing of the parallelogram, it will always start with the total method and then switch to the swap method and then back to the total method and so on.

### Python code
The Swap Method


```
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
...
```

The Total Method 


```
...
def totalMethod(x,y, maxi, minu):  
    #Going horizontally down
    if x == 0 or y == minu:
        return min(maxi, (x+y)), max((x+y-maxi), 0)
    #Going horizontally up
    else:
        return max((x+y-minu), 0), min(minu, (x+y))   

...
```
The calling

```
...
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
    if past == 0: # calls swapmethod
        x,y = swapMethod(x,y,tLength,sLength)
        past = 1
    else: #calls totalMethod
        x,y = totalMethod(x,y, tLength, sLength)
        past = 0
    history += f'{i+3:02} | {x} | {y} |\n'
print(history)
```
Full code [here](https://github.com/Dingo418/jug-solver/blob/6971860401a01b34b09d8b90eab4fa009b7fbf30/Basic%20bottle%20game.py)

### Closing notes
If you want to see a more complete version with inputs look on my GitHub [here](https://github.com/Dingo418/jug-solver).
Thanks to my math teacher for showing me this problem. It was a fun challenge.





