import numpy as np
import cv2
import os
from pathlib import Path

def adicionar_ruido_gaussiano(imagem, desvio_padrao):
    """Adiciona ruído gaussiano a uma imagem"""
    ruido = np.random.normal(0, desvio_padrao, imagem.shape)
    imagem_com_ruido = imagem.astype(np.float64) + ruido
    return np.clip(imagem_com_ruido, 0, 255).astype(np.uint8)

def criar_imagens_media(caminho_imagem, desvio_padrao, num_iteracoes, pasta_resultados):
    """Cria imagens com ruído e suas médias"""
    # Lê a imagem original
    original = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    
    # Cria diretório de resultados se não existir
    Path(pasta_resultados).mkdir(parents=True, exist_ok=True)
    
    # Salva imagem original
    cv2.imwrite(os.path.join(pasta_resultados, 'original.png'), original)
    
    # Inicializa soma para média
    soma_imagem = np.zeros_like(original, dtype=np.float64)
    
    # Gera imagens com ruído e suas médias acumuladas
    for i in range(num_iteracoes):
        # Adiciona ruído
        com_ruido = adicionar_ruido_gaussiano(original, desvio_padrao)
        
        # Salva imagem com ruído
        cv2.imwrite(os.path.join(pasta_resultados, f'ruido_{i+1}.png'), com_ruido)
        
        # Atualiza soma e calcula média
        soma_imagem += com_ruido
        media_atual = (soma_imagem / (i + 1)).astype(np.uint8)
        
        # Salva imagem média em pontos específicos
        if (i + 1) in [1, 5, 10, 20, 50, 100]:
            cv2.imwrite(os.path.join(pasta_resultados, f'media_{i+1}.png'), media_atual)

def main():
    # Define parâmetros
    caminho_imagem = 'img_example/pilares_da_criacao_original.png'
    desvios_padrao = [32, 64]
    num_iteracoes = 100
    
    for desvio_padrao in desvios_padrao:
        pasta_resultados = f'resultados/desvio_{desvio_padrao}'
        criar_imagens_media(caminho_imagem, desvio_padrao, num_iteracoes, pasta_resultados)
        print(f"Processamento completo para desvio_padrao={desvio_padrao}")

if __name__ == "__main__":
    main()