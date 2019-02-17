import matplotlib.pyplot as plt
import numpy as np
import math 
 #do not change makes all the circles
 #add one more for distance
def circle(center,rad):
    n = int(4*rad*math.pi)    
    t = np.linspace(0,6.3,n)      
    x = center[0]+rad*np.sin(t)   
    y = center[1]+rad*np.cos(t) 
    return x,y,
# modify to make it how it needs to be
def draw_circles(ax,n,center,radius,w,modifier):
    if n>0:
        modifier = modifier*w #changes the circle 
        
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax, n-1, [modifier, 0], radius*w, w, modifier)

plt.close("all") 
fig, ax = plt.subplots()
# copy from draw squares shapes to get the imput from the keyboard
try:
    n = int(input('how many recursive calls '))
except ValueError:
    print('Only numbers please')
    print('also no decimals')
    n = int(input('how many recursive calls '))
draw_circles(ax, n, [100,0], 100, .5, 100)    #change w to get the correct spacing .n will make it smaller on the wrong way so go with a normal intiger
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
