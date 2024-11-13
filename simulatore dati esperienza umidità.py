import random as rd

#NON MODIFICARE
indice_della_lista = 0

#viariabili globali
offset_max = 7
offset_min = 3
numero_di_pacchetti_simulati = 10000
space = 8
start_index = 2
end_index = 6
step = 2
'''
    DOCUMENTAZIONE:
    -La funzione simulatore() deve andare per come è stata pensata al posto della potetica lettura della porta usb 
    -Il codice necessario al simulatore è tutto quello superiore agli asterischi
    -Il codice al disotto della riga di asterischi serve solo per far capire l'output della funzione se si desidera si può cancellare senza compromettere nulla
    -Il valore delle variabili globali ad eccezzione dell'indice_della_lista è stato scelto ipotizzando quale potesse essere l'ipotetico output con cui ci interfacceremo
     durante l'esperienza, i valori possono essere cambiati qual'ora foste di idea diversa
    -L'unica cosa non accurata della simulazione è che non viene rispetta l'indivisibilità delle coppie di bit, questo non dovrebbe influire
     sulla struttura dei possibili codici ( se ritenete che invece sia diverso ditemelo che avrei comunque un'idea per implementare l'indivisibilità )
'''
def simulatore():
    global indice_della_lista,space,start_index,end_index,step

    f = indice_della_lista + space + rd.randint(start_index, end_index)
    c = dati[indice_della_lista:f]
    indice_della_lista = f
    if c==[]:
        return r'il tuo test dura troppo diminuire il tempo o aumentare il numero_di_pacchetti_simulati'

    return c



elementi = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f',]
dati = []

for f in range(rd.randint(offset_min,offset_max)):
    dati.append(elementi[rd.randint(0,len(elementi)-1)])

for i in range(numero_di_pacchetti_simulati):
    for s in range(4):
        dati.append('a')
    for i in range(8):
        dati.append(elementi[rd.randint(0,len(elementi)-1)])


#######################################################################################################################################################################################

for s in range(10000000):

    print(simulatore(),'\n')
