import os
import shutil


# Cria função

pasta_origem = r'.\LG'
pasta_destino = r'.\naousar\ReleaseToWMS'

for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.lower().endswith('.txt'):
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
        
        with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as arquivo:
            conteudo = arquivo.read()
            
        if 'RELEASE TO WMS' in conteudo:
            destino = os.path.join(pasta_destino, nome_arquivo)
            shutil.move(caminho_arquivo, destino)
            print(f'Movido: {nome_arquivo}')
