# Importação de bibliotecas

import time
import os
import datetime
import separaShipConfirm as shipConfirm

# Criando o timer de tarefas
def timer():
    while True:
        hora = datetime.datetime.now()
        print('🔍Verificando pasta...')
        print(hora)
        print()
        shipConfirm.separarWMS()
        time.sleep(60)
        

timer()