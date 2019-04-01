# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:25:26 2019

@author: djakd
"""

from ride import Ride
from vehicle import Vehicle
from operator import attrgetter

info = None
No_line = 0
rides_list = []
with open ("b_should_be_easy.in", "r") as fh:
    for line in fh:
        if No_line:
            inforide = line.split()
            start = (int(inforide[0]), int(inforide[1]))
            end = (int(inforide[2]), int(inforide[3]))
            earlieststart = int(inforide[4])
            latestfinish = int(inforide[5])
            rides_list.append(
                Ride(earlieststart, latestfinish, start, end, No_line-1)
                )
        else:
            info = line.split()

        No_line += 1

# print(info)
sorted_rides_list = sorted(rides_list, key=attrgetter('start'))
for ride in sorted_rides_list:
    print(ride)
vehicles_list = [Vehicle((0,0)) for i in range(100)]

out = open("b_should_be_easy.out", "w")
r=0

for i in range(349):
    line = "28"
    for j in range(28):
        line += " "+str(j)
    line += "\n"

    out.write("28"+" "+ str(r) +" "+ str(r+1)+" "+ str(r+2)+"\n")

    r += 28
#out.write("3"+" "+ str(r) +" "+ str(r+1)+" "+ str(r+2))

line = "28"
for j in range(28):
    line += " " + str(j)
line += "\n"

out.write("28" + " " + str(r) + " " + str(r + 1) + " " + str(r + 2) + "\n")




out.close()






