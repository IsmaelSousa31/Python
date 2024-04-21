hora = int(input('Que horas são: '))

if(hora <= 11 ):
    print('Bom dia')
elif(hora >= 12) and (hora <= 17):
    print('Boa tarde')
elif(hora <= 23) and (hora >= 18):
    print('Boa noite')