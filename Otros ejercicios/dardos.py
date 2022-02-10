import random
puntaje=0
cont=0
total=0
while cont <= 4:
    print('Disparo dardo N°: '+str(cont+1))
    puntos = random.randint(0,100)
    
    if puntos==0:
        print('obtuviste 500')
        print('sacaste: '+str(puntos))
        puntaje=500
        
    elif puntos >=1 and puntos<=10:
        print ('obtuviste 450')
        print('sacaste: '+str(puntos))
        puntaje=450
        
        
    elif puntos >=11 and puntos<=20:
        print ('obtuviste 400')
        print('sacaste: '+str(puntos))
        puntaje=400
        
        
    elif puntos >=21 and puntos<=30:
        print ('obtuviste 350')
        print('sacaste: '+str(puntos))
        puntaje=350
        
        
    elif puntos >=31 and puntos<=40:
        print ('obtuviste 300')
        print('sacaste: '+str(puntos))
        puntaje=300
        
        
    elif puntos >=41 and puntos<=50:
        print ('obtuviste 250')
        print('sacaste: '+str(puntos))
        puntaje=250
        
        
    elif puntos >=51 and puntos<=60:
        print ('obtuviste 200')
        print('sacaste: '+str(puntos))
        puntaje=200
        
        
    elif puntos >=61 and puntos<=70:
        print ('obtuviste 150')
        print('sacaste: '+str(puntos))
        puntaje=150
        
        
    elif puntos >=71 and puntos<=80:
        print ('obtuviste 100')
        print('sacaste: '+str(puntos))
        puntaje=100
        
        
    elif puntos >=81 and puntos<=90:
        print ('obtuviste 50')
        print('sacaste: '+str(puntos))
        puntaje=50
        
        
    elif puntos >=91 and puntos<=100:
        print ('fallaste')
        print('sacaste: '+str(puntos))
        puntaje=0
        
    cont+=1
    total=total+puntaje
print('Saco un total de: '+str(total))
    