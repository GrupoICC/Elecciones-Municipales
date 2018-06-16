def NumeroMesas():
    munivotantes=[]
    muni = input('Ingrese el nombre de la municipalidad: ')
    munimesas={muni:munivotantes}
    mesas = int(input('Ingrese el número de mesas: '))
    for i in range(mesas):
        votantes = int(input('Ingrese el número de votantes de la mesa '+str(i+1)+': '))
        munivotantes.append(votantes)
    return munimesas
NumeroMesas()
