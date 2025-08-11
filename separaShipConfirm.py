import os
import shutil


# Cria função
def separarWMS ():

    pasta_origem = r'.\LG'
    pasta_destinoWMS = r'.\naousar'
    pasta_destinoSHIP = r'.\usar'
    pasta_indefinido = r'.\indefinido'

    for nome_arquivo in os.listdir(pasta_origem):
        if nome_arquivo.lower().endswith('.txt'):
            caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
            
            with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as arquivo:
                conteudo = arquivo.read()
                
            if 'RELEASE TO WMS' in conteudo:                                    # Procura pelo RELEASE TO WMS dentro do arquivo
                destino = os.path.join(pasta_destinoWMS, nome_arquivo)          # Mostra o caminho da pasta de destino do arquivo
                shutil.move(caminho_arquivo, destino)                           # Efetivamente move o arquivo para a outra pasta
                print(f'WMS Movido: {nome_arquivo}')                            # Visual para informar que foi movido
            
            elif 'SHIP CONFIRM' in conteudo:                                    # Procura pelo RELEASE TO WMS dentro do arquivo
                destino = os.path.join(pasta_destinoSHIP, nome_arquivo)         # Mostra o caminho da pasta de destino do arquivo
                shutil.move(caminho_arquivo,destino)                            # Efetivamente move o arquivo para a outra pasta
                print(f'SHIP Movido: {nome_arquivo}')                           # Visual para informar que foi movido
            
            else:                                                               # Caso não se adeque nos demais
                destino = os.path.join(pasta_indefinido, nome_arquivo)          # Mostra o caminho da pasta de destino do arquivo
                shutil.move(caminho_arquivo, destino)                           # Efetivamente move o arquivo para a outra pasta
                print(f'INDEFINIDO Movido: {nome_arquivo}')                     # Visual para informar que foi movido
