
#PERSONAS = 10
#LIMITE_CUENTA = 25

PERSONAS = int(input("ingresar cantidad de personas: "))
LIMITE_CUENTA = int(input("ingresar limite de cuenta: "))

cuenta = 0
persona = 0
giro = "horario"

        

if (LIMITE_CUENTA < PERSONAS):
    print ("error")

else:

    for ciclo in range(LIMITE_CUENTA):
        cuenta = cuenta + 1 # contador general
        

        if (giro == "horario"):
            if (persona == PERSONAS):
                persona = 0
            persona = persona + 1 # contador persona
        else:
            if (persona == 1):    
                persona = PERSONAS + 1
            persona = persona - 1 # contador de persona    

        print (persona, cuenta)



        if (cuenta % 8 == 0): #es perfectamente divisible por 8
            if (giro == "horario"):
                giro = "antihorario"
            else:
                giro = "horario" 

            #print ("divisible")
        
        if (cuenta % 11 == 0): #es perfectamente divisible por 8

            print ("divisible por 11")

            cuenta = cuenta + 1

            
            