# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 08:21:57 2022

@author: Roni
Attack on pseudorandomness
"""
import numpy
from random import random,randint,seed,shuffle
import time
start_time = time.time()


interval=[]#this represents all the possible time differences within the given
#boundaries on the time differences
seedList=[]#This list represents all the possible time differences that generates 
#a sequence that matches at least the first 10% of Alice's sequence
for i in range(1000000):
    interval.append(i)
shuffle(interval)

l_1=numpy.zeros(1000,int)
l_2=numpy.zeros(1000,int)
"""l_1 and l_2 respectively represents the two Pseudorandomly generated sequences
of Alice and Eve"""
time_M1=1500 + randint(0, 1000000)
time_M2=1100
"""we supposed that the adversary have some knowledge on the opponent’s time reference
such as the approximate time zone. time_M1 represents Alice's time reference,
while time_M2 represents Eve's time reference """
print("hello")
seed(time_M1)
for i in range(1000):
    l_1[i]=randint(0, 1)
for k in interval:
    seed(time_M2+k)
    for i in range(1000):
        l_2[i]=randint(0, 1)

    for i in range(100):
        if l_1[i]!=l_2[i]:
            break
        elif l_1[i]==l_2[i]:
            seedList.append(k)
    
print("--- %s seconds ---" % (time.time() - start_time))
"""Once Alice reveals her basis choices, Eve can proceed into comparing all 
possible seeds then check which of them generates the same choices. Eve can then 
deduce the time difference and to adjust her machine's time accordingly """