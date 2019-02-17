import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1]
        ax.plot(p[:,0],p[:,1],color='k')
        #need quarters of 800
        tr = 600 + p[i1]*.5
        draw_squares(ax,n-1,tr,.5)
        tl = [-200, 600] + p[i1]*.5   
        draw_squares(ax,n-1,tl,.5)
        br = [600, -200] + p[i1]*.5   
        draw_squares(ax,n-1,br,.5)
        bl = -200 + p[i1]*.5          
        draw_squares(ax,n-1,bl,.5)


plt.close("all")
orig_size = 800
p = np.array([[0,0], [0, orig_size], [orig_size, orig_size], [orig_size, 0], [0, 0]])# do not change
fig, ax = plt.subplots()
#will only work once
try:
    n = int(input('how many recursive calls '))
except ValueError:
    print('Only numbers please')
    print('also no decimals')
    n = int(input('how many recursive calls '))
draw_squares(ax, n, p, .5)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('squares.png')
#p are the points
#n is the recursive calls
#w is where the smaller square gets the bigger square run through it