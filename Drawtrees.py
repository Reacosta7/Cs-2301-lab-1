import numpy as np
import matplotlib.pyplot as plt
import math 

def draw_trees(ax,n,p,w):
    if n>0:
        i1 = [1,2,3,0,1]
        #q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        lt = [0,0] + p[i1]*.5
        draw_trees(ax,n-1,lt,w)
        rt = [400,0] + p[i1]*.5
        draw_trees(ax,n-1,rt,w)
        
    
plt.close("all")
orig_size = 800
p = np.array([[0,0],[0,0],[orig_size/2,orig_size/2],[orig_size,0],[orig_size,0]])
fig, ax = plt.subplots()
try:
    n = int(input('how many recursive calls '))
except ValueError:
    print('Only numbers please')
    print('also no decimals')
    n = int(input('how many recursive calls '))
draw_trees(ax,n,p,.5)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('trees.png')
#def draw_squares(ax,n,p,w):
#    if n>0:
#        i1 = [0,1,2,3,0,1]
#        q = p*w + p[i1]*(1-w)
#        ax.plot(p[:,0],p[:,1],color='k')
#        draw_squares(ax,n-1,q,w)

#plt.close("all") 
#orig_size = 800
#p = np.array([[0,0],[0,orig_size],[orig_size,0],[0,0]])
#fig, ax = plt.subplots()
#draw_squares(ax,15,p,1)
#ax.set_aspect(1.0)
#ax.axis('off')
#plt.show()
#fig.savefig('squares.png')