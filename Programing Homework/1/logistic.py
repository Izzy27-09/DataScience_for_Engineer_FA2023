#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import math

r = .5
x = np.zeros(31)
x[0] = .75 # np arrays are mutable
for i in range(30): # 0, 1, ... 29
    x[i+1] = r*x[i]*(1-x[i])
    
plt.plot(range(31),x)
plt.xlabel('Iteration')
plt.ylabel('State')
plt.title('Evolution for r=0.5 and x0 = 0.75')
plt.savefig('figure1.pdf')
plt.savefig('figure1.png')




# In[2]:


r = [.5,0.15,0.85]
x = np.zeros(31)
for d in range(len(r)):
    x[0] = .75 # np arrays are mutable
    for i in range(30):# 0, 1, ... 29
        x[i+1] = r[d]*x[i]*(1-x[i])
    plt.plot(range(31),x)
    
plt.legend(r)
plt.xlabel('Iteration')
plt.ylabel('State')
plt.title('Evolution for r=0.5,0.15,0.85 and x0 = 0.75')
plt.savefig('figure2.pdf')
plt.savefig('figure2.png')


# In[3]:


r = 1.75
x = np.zeros(31)
x[0] = .75 # np arrays are mutable
for i in range(30): # 0, 1, ... 29
    x[i+1] = r*x[i]*(1-x[i])
    
plt.plot(range(31),x)
plt.xlabel('Iteration')
plt.ylabel('State')
plt.title('Evolution for r=1.75 and x0 = 0.75')
plt.savefig('figure3.pdf')
plt.savefig('figure3.png')


# In[4]:


r = 2.75
x[0] = .75 # np arrays are mutable
for i in range(30): # 0, 1, ... 29
    x[i+1] = r*x[i]*(1-x[i])
    
plt.plot(range(31),x)
plt.xlabel('Iteration')
plt.ylabel('State')
plt.title('Evolution for r=2.75 and x0 = 0.75')
plt.savefig('figure4.pdf')
plt.savefig('figure4.png')


# In[5]:


r = 3.5
x[0] = .75 # np arrays are mutable
for i in range(30): # 0, 1, ... 29
    x[i+1] = r*x[i]*(1-x[i])
    
plt.plot(range(31),x)
plt.xlabel('Iteration')
plt.ylabel('State')
plt.title('Evolution for r=3.5 and x0 = 0.75')
plt.savefig('figure5.pdf')
plt.savefig('figure5.png')


# In[6]:


r = 3.8
x[0] = .75 # np arrays are mutable
for i in range(30): # 0, 1, ... 29
    x[i+1] = r*x[i]*(1-x[i])
    
plt.plot(range(31),x)
plt.xlabel('Iteration')
plt.ylabel('State')
plt.title('Evolution for r=3.8 and x0 = 0.75')
plt.savefig('figure6.pdf')
plt.savefig('figure6.png')


# In[7]:


converges={}
r=[ 0.15,0.5,0.85,1.75,2.75,3.5,3.8]
x=np.linspace(0,4,1500)
for d in range(len(r)):
    x[0]=0.75
    for i in range(1499):
        x[i+1]=r[d]*(1-x[i])
    if((x[1499]<10**-7) or abs(x[1499]-x[1498])/x[1499]<0.0001):
         converges.update({r[d]: 1})
    else:
        #con_not.append(r)
        converges.update({r[d]: 0})
        
lists = sorted(converges.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.yticks([0, 1], ['Does Not Converge', 'Converges'])
plt.ylabel('Converges/Not Converges')
plt.title('R values that converges and does not converge')
plt.xlabel('R-Values')
plt.scatter(x,y,marker="o",color="red",alpha=0.5)
plt.xlabel('R-Values')
plt.savefig('figure7.pdf')
plt.savefig('figure7.png')


# In[17]:


converges_plot={}
r_plot={}
r=[ 0.15,0.5,0.85,1.75,2.75,3.5,3.8]
x=np.linspace(0,4,1500)
for d in range(len(r)):
    x[0]=0.75
    for i in range(1499):
        x[i+1]=r[d]*(1-x[i])
    if((x[1499]<10**-7) or abs(x[1499]-x[1498])/x[1499]<0.0001):
        
        converges_plot.update({r[d]:x[1499]})
        r_plot.update({((r[d]-1)/r[d]):x[1499]})
        
    else:
        r_plot.update({((r[d]-1)/r[d]):x[1499]})
        converges_plot.update({r[d]:-0.1})

list_1 = sorted(converges_plot.items())
x_1, y_1 = zip(*list_1) # Holds points for the limit at f(r)

for key in r_plot:
    if(math.isinf(r_plot[key])):
        r_plot[key]=-0.1

list_2 = sorted(r_plot.items()) 
x_2, y_2 = zip(*list_2) # Holds points for (r-1)/r

fig, ax = plt.subplots()
ax.plot(x_1, y_1, label='f(r)',marker='x')
ax.plot(x_2, y_2, label='(r-1)/r', marker='s', color='r')
ax.legend()
plt.ylabel('Output Value')
plt.xlabel('Input Value')
plt.title("Graph showing the out puts of r and (r-1)/r")
plt.savefig('figure8.pdf')
plt.savefig('figure8.png')
        
            
        
        
    


# In[ ]:




