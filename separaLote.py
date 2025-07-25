import os
import shutil

origem = r'.\LG'
destino_base = r'.\separado'

contador_arquivos = 0
contador_lote = 1

# Garante que o destino base existe
os.makedirs(destino_base, exist_ok=True)

while os.listdir(origem):
    # Cria a pasta do lote atual
    destino_lote = os.path.join(destino_base, f"lote_{contador_lote}")
    os.makedirs(destino_lote, exist_ok=True)

    arquivos = [f for f in os.listdir(origem) if f.lower().endswith('.txt')]

    if not arquivos:
        break  # Se não há mais arquivos .txt, finaliza

    for nomeArquivo in arquivos:
        if contador_arquivos == 100:
            break  # Limita a 100 arquivos por lote

        origem_arquivo = os.path.join(origem, nomeArquivo)
        destino_arquivo = os.path.join(destino_lote, nomeArquivo)

        shutil.move(origem_arquivo, destino_arquivo)
        contador_arquivos += 1

    contador_lote += 1
    contador_arquivos = 0
