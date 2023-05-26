# YOLO
Object detection and image processing

## Estrutura de pastas
```
.
├── cracks/
│   ├── assets/
│   │   ├── 9ea1d4d6-cc21-48dc-b214-a09e26f436961627385689.webp
│   │   └── results.jpg
│   ├── best.pt
│   ├── Cracks.ipynb
│   ├── imgyolo.py
│   └── yolo.py
├── pokemon/
│   ├── poke.pt
│   ├── Pokemon.ipynb
│   └── pokeYolo.py
└── README.md
```

### Cracks
Esta pasta contém os arquivos de imagem para os testes do yolo, bem como os scripts em python & Jupyter Notebook usado para treinar o modelo.

### Pokemon
Esta pasta contém testes utilizando um modelo treinado com dataset de pokemon do roboflow.

## Arquivos .pt
Os arquivos .pt foram gerados a partir dos arquivos .ipynb utilizando o Google Colab. O treino leva cerca de 20 minutos.

## Arquivos .py
Estes arquivos servem para rodar o OpenCV juntamente com os modelos gerados. Rode os arquivos para fazer as detecções.
