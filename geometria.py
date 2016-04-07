import random
import math

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
#    print (' nem megszerkeszthető')
#else:
#    print ('megszerkeszthető')
print('Legyenek egy háromszög oldalai, a = {0} cm, b={1} cm és c = {2} cm.'.format(oldalak[0], oldalak[1], oldalak[2]))
#haromszog
def h_kerulet():
    ker=0
    for i in range(3):
        ker+=oldalak[i]
    return ker
    
def h_terulet():
    s=0
    for i in range(3):
        s+=oldalak[i]
    s=s/2
    return math.sqrt(s*(s-oldalak[0])*(s-oldalak[1])*(s-oldalak[2]))        
    ter=0
    return ter
#téglalap
def t_kerulet():
    t_ker=2*oldalak[0]+2*oldalak[1]
    return t_ker
    
def t_terulet():
    t_ter=oldalak[0]*oldalak[1]
    return t_ter
#négyzet
def n_kerulet():
    n_ker=4*oldalak[0]
    return n_ker
    
def n_terulet():
    n_ter=math.sqrt (oldalak[0])
    return t_ter
    
print ('Háromszög kerülete: {0:.2f}'.format(h_kerulet()))
print ('Háromszög területe: {0:.2f}'.format (h_terulet()))    
print ('Téglalap kerülete: {0:.2f}'.format(t_kerulet()))
print ('Téglalap területe: {0:.2f}'.format (t_terulet()))
print ('Négyzet kerülete: {0:.2f}'.format (n_kerulet()))
print ('Négyzet területe: {0:.2f}'.format (n_terulet()))
