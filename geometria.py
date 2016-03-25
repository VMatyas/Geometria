# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 12:10:35 2016

@author: Gabor
"""

import random

oldalak = list()
oldalak.append(random.randrange(1,50))
oldalak.append(random.randrange(1,50))
intervall_felso=oldalak[0]+oldalak[1]+2
if oldalak[0]>oldalak[1] :
    intervall_also = oldalak[0]-oldalak[1]
else:
    intervall_also = oldalak[1]-oldalak[0]

oldalak.append (random.randrange(intervall_also,intervall_felso))

#print ('alsó határ {0}'.format(intervall_also))
#print ('felső határ {0}'. format(intervall_felso))
#if oldalak[0]>oldalak[1]+oldalak[2] or oldalak[1]>oldalak[0]+oldalak[2] or oldalak[2]>oldalak[0]+oldalak[1]:
#    print (' nem megszekeszthető')
#else:
#    print ('megszekeszthető')
print('Legyenek egy háromszög oldalai, a = {0} cm, b={1} cm és c = {2} cm.'.format(oldalak[0], oldalak[1], oldalak[2]))