import random
import math
import sys


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
milyenalakzat = input('Háromszöget (H), vagy négyszöget (N) választ? (Kilépés:Q) ' )
while (milyenalakzat!='H' or milyenalakzat!='N'):
    milyenalakzat = input('Háromszöget (H), vagy négyszöget (N) választ?  (Kilépés:Q) ' )
    if milyenalakzat == 'H':
        helyes=0;
        print('Legyenek egy háromszög oldalai, a = {0} cm, b={1} cm és c = {2} cm.'.format(oldalak[0], oldalak[1], oldalak[2]))
        #haromszog
        def h_kerulet():
            h_ker=0
            for i in range(3):
                h_ker+=oldalak[i]
            return h_ker
    
        def h_terulet():
            s=0
            for i in range(3):
                s+=oldalak[i]
            s=s/2
            return math.sqrt(s*(s-oldalak[0])*(s-oldalak[1])*(s-oldalak[2]))        
            h_ter=0
            return h_ter

        ellenorzo_kerulet = h_kerulet()
        haromszoge = input('A fenti adatokból kirajzolható alakzat egyenlőszárú (E), vagy nem egyenlőszárú (N) lehet? ')
        if haromszoge=='E' and oldalak[0]==oldalak[1]:
            print ('Helyes válasz, az alakzat tényleg egyenlő szárú háromszög!')
            helyes=helyes+1
        elif haromszoge=='E' and oldalak[0]!=oldalak[1]:
            print ('Helytelen válasz, az alakzat nem egyenlő szárú háromszög!')
        elif haromszoge=='N' and oldalak[0]!=oldalak[1]:
            print ('Helyes válasz, az alakzat nem egyenlő szárú háromszög!')
            helyes=helyes+1
        elif haromszoge=='N' and oldalak[0]==oldalak[1]:
            print ('Helytelen válasz, az alakzat egyenlő szárú háromszög!')
            
        kiszamolt_kerulet = int(input('Hány cm a háromszög kerülete? '))
        if kiszamolt_kerulet == h_kerulet() :
            print ('Helyes válasz, a háromszög kerülete valóban {0:.2f} cm.'.format(h_kerulet()))
            helyes=helyes+1
        else:
            print ('Sajnos a válasz helytelen, a háromszög kerülete {0:.2f} cm.'.format(h_kerulet()))

        kiszamolt_terulet = input('Hány cm^2 a háromszög területe? ')
        if kiszamolt_terulet==h_terulet():
            print ('Helyes válasz, a háromszög területe valóban {0:.2f} cm^2.'.format(h_terulet()))
            helyes=helyes+1
        else:
            print ('Sajnos a válasz helytelen, a háromszög területe {0:.2f} cm^2.'.format(h_terulet()))

        print ('Háromszög kerület: {0:.2f}'.format(h_kerulet()))
        print ('Háromszög terület: {0:.2f}'.format (h_terulet()))
        print ('Helyes válaszok száma: {0}'.format(helyes))
           
    elif milyenalakzat == 'N':
        #téglalap
        print('Legyenek egy négyszög oldalai, a = {0} cm, b = {1} cm.'.format(oldalak[0], oldalak[1]))
        helyes=0;
        def t_kerulet():
            t_ker=2*oldalak[0]+2*oldalak[1]
            return t_ker
    
        def t_terulet():
            t_ter=oldalak[0]*oldalak[1]
            return t_ter
        
        ellenorzo_kerulet = t_kerulet()
        negyzete = input('A fenti adatokból kirajzolható alakzat négyzet (N), vagy téglalap (T) lehet? ')
        if negyzete=='N' and oldalak[0]==oldalak[1]:
            print ('Helyes válasz, az alakzat tényleg négyzet!')
            helyes=helyes+1
        elif negyzete=='N' and oldalak[0]!=oldalak[1]:
            print ('Helytelen válasz, az alakzat nem négyzet!')
        elif negyzete=='T' and oldalak[0]!=oldalak[1]:
            print ('Helyes válasz, az alakzat tényleg téglalap!')
            helyes=helyes+1
        elif negyzete=='T' and oldalak[0]==oldalak[1]:
            print ('Helytelen válasz, az alakzat nem téglalap!')
            
        kiszamolt_kerulet = int(input('Hány cm a négyszög kerülete? '))
        if kiszamolt_kerulet == t_kerulet() :
            print ('Helyes válasz, a négyszög kerülete valóban {0:.2f} cm.'.format(t_kerulet()))
            helyes=helyes+1
        else:
            print ('Sajnos a válasz helytelen, a négyszög kerülete {0:.2f} cm.'.format(t_kerulet()))

        kiszamolt_terulet = input('Hány cm^2 a négyszög területe? ')
        if kiszamolt_terulet==t_terulet():
            print ('Helyes válasz, a négyszög területe valóban {0:.2f} cm^2.'.format(t_terulet()))
            helyes=helyes+1
        else:
            print ('Sajnos a válasz helytelen, a négyszög területe {0:.2f} cm^2.'.format(t_terulet()))
            
            print ('Téglalap kerület: {0:.2f}'.format(t_kerulet()))
            print ('Téglalap terület: {0:.2f}'.format (t_terulet()))
            print ('Helyes válaszok száma: {0}'.format(helyes))
    elif milyenalakzat == 'Q':
        sys.exit('Viszlát')
