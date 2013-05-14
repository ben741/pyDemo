# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:11:33 2013

@author: Ben
"""

from __future__ import division 
import time

for word in ['Hello', 'world!']:
    
    #check if math is true
    if not 1/2 == 0:
        print word

print "finished at " + time.asctime(time.localtime())