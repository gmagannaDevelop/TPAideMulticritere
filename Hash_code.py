#!/usr/bin/env python
# coding: utf-8

# In[22]:


import math
import numpy as np
import os


# In[2]:


ls Datasets-20190325/


# In[32]:


class Vehicule(object):
    """ Représenter un véhicule avec sa position.
    """
    
    def __init__(self, point, free=True):
        self.x = point[0]
        self.y = point[1]
        self.free = True
        self.trajets = []
        self.completed = []
    
    @property
    def n_completed_trips(self):
        return len(self.completed)

    @property
    def completed_trips(self):
        return [vehicule.number for vehicule in self.completed]
    
    @property
    def position(self):
        return (self.x, self.y)
    
    @property
    def is_free(self):
        return self.free
    
    def occupy(self):
        self.free = False
    
    def add_trip(self, trip):
        self.occupy()
        self.trajet.append(trip)
    
    def get_distance(self, point):
        """ Calcule la distance de la position actuelle du vehicule
        au point desiré. 
        """
        return np.abs(point[0] - self.x) + np.abs(point[1] - self.y)
    
    def move(self):
        if self.position != self.trajets[-1].start:
            pass
    
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

    '''
    def _finish(self, point):
        pas_x = math.copysign(1, point[0] - self.x)
        pas_y = math.copysign(1, point[1] - self.y)
        while self.x != point[0]:
            self.x += pas_x
            print(f'({self.x}, {self.y})')
        while self.y != point[1]:
            self.y += pas_y
            print(f'({self.x}, {self.y})')
    '''


# In[29]:


class Trajet(object):
    """
    """
    
    def __init__(self, number, start, finish, earliest, latest, completed=False):
        self._number = number
        self.start = start
        self.finish = finish 
        self.earliest = earliest
        self.latest = latest
        self.completed = completed
    
    @property
    def number(self):
        return self._number
    
    def get_distance(self, point):
        return np.abs(point[0] - self.x) + np.abs(point[1] - self.y)
    
    def get_closest(self, cars):
        _tmp = (x.position for x in cars)
        distances = list(map(self.get_distance, _tmp))
        idx = distances.index(min(distances))
        return idx
    
    def assign(self, car):
        car
    
    
        


# In[25]:


infile = 'Datasets-20190325/b_should_be_easy.in'
outfile = (os.path.split(infile)[1]).replace('in', 'out')


# In[27]:


with open(infile, 'r') as f:
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
                'number': i,
                'start': start,
                'finish': finish, 
                'earliest': earliest,
                'latest': latest
            })


# In[21]:


len(trajets)


# In[34]:


vehicules = [Vehicule((0, 0)) for i in range(vehicles)]


# In[ ]:





# In[39]:


with open(outfile, 'w') as f:
    for vehicule in vehicules:
        f.write(f'{vehicule.n_completed_trips} ')
        for trip in vehicule.completed_trips:
            f.write(f'{trip} ')
        f.write('\n')


# In[40]:


cat b_should_be_easy.out


# In[ ]:





# In[ ]:





# In[ ]:




