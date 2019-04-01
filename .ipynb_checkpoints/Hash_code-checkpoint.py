#!/usr/bin/env python
# coding: utf-8

# In[53]:


import math
import numpy as np


# In[2]:


ls Datasets-20190325/


# In[119]:


class Vehicule(object):
    """ Représenter un véhicule avec sa position.
    """
    
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]
     
    @property
    def position(self):
        return (self.x, self.y)
    
    def get_distance(self, point):
        """ Calcule la distance de la position actuelle du vehicule
        au point desiré. 
        """
        return np.abs(point[0] - self.x) + np.abs(point[1] - self.y)
    
    def _finish(self, point):
        pas_x = math.copysign(1, point[0] - self.x)
        pas_y = math.copysign(1, point[1] - self.y)
        while self.x != point[0]:
            self.x += pas_x
            print(f'({self.x}, {self.y})')
        while self.y != point[1]:
            self.y += pas_y
            print(f'({self.x}, {self.y})')
            
    def move_x(self, point):
        if self.x != point[0]:
            pas_x = math.copysign(1, point[0] - self.x)
            self.x += pas_x
        return self.position
    
    def move_y(self, point):
        if self.y != point[1]:
            pas_y = math.copysign(1, point[1] - self.y)
            self.y += pas_y
        return self.position


# In[123]:


class Trajet(object):
    """
    """
    
    def __init__(self, start, finish, earliest, latest):
        self.start = start
        self.finish = finish 
        self.earliest = earliest
        self.latest = latest
    
    def get_distance(self, point):
        return np.abs(point[0] - self.x) + np.abs(point[1] - self.y)
    
    def get_closest(self, cars):
        _tmp = (x.position for x in cars)
        min(map(self.get_distance, _tmp))
        return 0
    [car0, car1, car2]
        


# In[110]:


with open('Datasets-20190325/b_should_be_easy.in', 'r') as f:
    trajets = []
    for i, line in enumerate(f):
        _tmp = list(map(int, line.split(' ')))
        if i == 0:
            rows, columns, vehicles, rides, bonus, steps = _tmp
        else:
            start  = (_tmp[0], _tmp[1])
            finish = (_tmp[2], _tmp[3])
            earliest = _tmp[4]
            latest = _tmp[5]
            
            trajets.append({
                'start': start,
                'finish': finish, 
                'earliest': earliest,
                'latest': latest
            })


# In[112]:


len(trajets)


# In[113]:


vehicules = [Vehicule((0, 0)) for i in range(vehicles)]


# In[ ]:


for i in range(steps):
    


# In[121]:


min(map(lambda x: x, [i for i in range(10)]))


# In[124]:


[ for i in range(20)]


# In[ ]:





# In[ ]:





# In[ ]:




