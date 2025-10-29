# Processamento de Imagem com Ruído Gaussiano

Este projeto implementa um gerador de ruído gaussiano e sistema de média para imagens em tons de cinza. Ele demonstra como o ruído aleatório pode ser reduzido através da média de imagens.

## Visão Geral

O programa realiza as seguintes operações:
1. Carrega uma imagem em tons de cinza
2. Aplica ruído gaussiano com desvios padrão específicos (32 e 64)
3. Gera múltiplas versões com ruído da imagem original
4. Calcula médias acumuladas das imagens com ruído
5. Salva tanto as imagens com ruído quanto as médias

### Resultados Esperados

O programa gera dois conjuntos de resultados (para σ=32 e σ=64):
- Imagem original
- Imagens individuais com ruído (100 versões)
- Imagens médias em iterações específicas (1, 5, 10, 20, 50, 100)

À medida que mais imagens são calculadas na média, você notará a redução do ruído mantendo as características da imagem original.

## Instalação e Uso

1. Crie e ative um ambiente virtual:
```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Instale as dependências:
```bash
pip install numpy==1.24.3
pip install opencv-python==4.8.1.78
```

3. Execute o programa:
```bash
python python/source.py
```

Os resultados serão salvos em `python/resultados/`.

## Estrutura do Projeto
```
tec433_ruido_gaussiano/
├── python/
│   ├── source.py
│   └── resultados/
├── img_example/
│   └── pilares_da_criacao_original.png
└── README.md
```

## Requisitos

- Python 3.12.6
- NumPy 1.26.2
- OpenCV-Python 4.8.1.78