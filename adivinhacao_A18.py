import random 
import os
erros = 0
pc =random.randrange(0,100)
user = int(input("Numero que vc acha "))
os.system('cls')
while(pc!=user):
    if(user>pc):
        print('Chutou alto')
    else:
        print('Chutou baixo')
    erros+=1
    user = int(input('Proxima tentativa '))

print(f'Acerto, vc demorou {erros} tentativas para acertar')