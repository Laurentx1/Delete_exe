import os
import time

# Caminho da pasta onde estão os executáveis
pasta = r"C:\Program Files (x86)\Horus\Executaveis"

# Lista de arquivos para deletar
arquivos_para_deletar = ["Compras.exe", "Contabil.exe"]

def deletar_arquivos():
    for arquivo in arquivos_para_deletar:
        caminho = os.path.join(pasta, arquivo)
        if os.path.exists(caminho):
            try:
                os.remove(caminho)
                print(f"[OK] Arquivo deletado: {caminho}")
            except Exception as e:
                print(f"[ERRO] Não foi possível deletar {caminho}: {e}")
        else:
            print(f"[INFO] Arquivo não encontrado: {caminho}")

if __name__ == "__main__":
    # Espera alguns segundos para garantir que o Windows terminou de carregar
    time.sleep(5)
    deletar_arquivos()

