[English]

# League of Legends Auto Accept

League of Legends Auto Accept is an automated tool to quickly and efficiently accept matches in League of Legends. Using image recognition, the program detects the "Accept" button on the screen and clicks it automatically, so you don't miss matches by failing to accept in time.

## Features

- **Automatic match acceptance**: Detects and clicks the "Accept" button as soon as it appears.
- **Simple graphical interface**: Choose the language and easily enable/disable auto accept.
- **Multi-language support**: Currently supports Portuguese and English.
- **Compatible with Windows** (cx_Freeze configured to generate executable).

## Installation

### Prerequisites

- Python 3.7+
- Pip

### Dependencies

Install the required dependencies:

```
pip install -r requirements.txt
```

If there is no `requirements.txt` file, install manually:

```
pip install pyautogui opencv-python numpy
```

### Running from source

1. Clone the repository:
    ```
    git clone https://github.com/CarlosFeliponi/League-of-Legends_Auto_Accept.git
    cd League-of-Legends_Auto_Accept
    ```

2. Run the program:
    ```
    python main.py
    ```

### Building Executable (Windows)

1. Install cx_Freeze:
    ```
    pip install cx_Freeze
    ```

2. Build the executable:
    ```
    python setup.py build
    ```

The executable will be in the `build` folder.

## Project Structure

```
LolAutoAccept/
├── Languages/
│   ├── Option.txt
│   ├── Portuguese/
│   │   ├── accept.png
│   │   └── notaccept.png
│   └── English/
│       ├── accept.png
│       └── notaccept.png
├── main.py
├── setup.py
└── README.md
```

- **main.py**: Main application code.
- **setup.py**: Script to generate executable with cx_Freeze.
- **Languages/**: Directory with language options and reference images for button recognition.

## How to use

1. Open League of Legends and go to the match search screen.
2. Run LOL Auto Accept.
3. Select the desired language.
4. Click "ON" to activate auto accept.
5. The program will monitor the screen. When the "Accept" button appears, it will be clicked automatically.

## Adding a new language

1. Create a new folder inside `Languages/` with the name of the language.
2. Add the `accept.png` and `notaccept.png` images for the "Accept" button and the "Not Accepted" state in that language.
3. Add the language to the list in `Languages/Option.txt`.

## Notes

- The program uses image recognition, so the reference images must be exact screenshots of the button in your resolution and language.
- You may need to run as administrator for the click to work properly on some systems.

## Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

[Portugues]

# League of Legends Auto Accept

League of Legends Auto Accept é uma ferramenta automatizada para aceitar partidas no League of Legends de forma rápida e eficiente. Utilizando reconhecimento de imagem, o programa detecta o botão "Aceitar" na tela e clica automaticamente, evitando que você perca partidas por não aceitar a tempo.

## Funcionalidades

- **Aceitação automática de partidas**: Detecta e clica no botão "Aceitar" assim que ele aparece.
- **Interface gráfica simples**: Escolha o idioma e ative/desative o auto accept facilmente.
- **Suporte a múltiplos idiomas**: Atualmente suporta Português e Inglês.
- **Compatível com Windows** (cx_Freeze configurado para gerar executável).

## Instalação

### Pré-requisitos

- Python 3.7+
- Pip

### Dependências

Instale as dependências necessárias:

```
pip install -r requirements.txt
```

Se não houver um arquivo `requirements.txt`, instale manualmente:

```
pip install pyautogui opencv-python numpy
```

### Executando via código-fonte

1. Clone o repositório:
    ```
    git clone https://github.com/CarlosFeliponi/League-of-Legends_Auto_Accept.git
    cd League-of-Legends_Auto_Accept
    ```

2. Execute o programa:
    ```
    python main.py
    ```

### Gerando Executável (Windows)

1. Instale o cx_Freeze:
    ```
    pip install cx_Freeze
    ```

2. Gere o executável:
    ```
    python setup.py build
    ```

O executável estará na pasta `build`.

## Estrutura do Projeto

```
LolAutoAccept/
├── Languages/
│   ├── Option.txt
│   ├── Portuguese/
│   │   ├── accept.png
│   │   └── notaccept.png
│   └── English/
│       ├── accept.png
│       └── notaccept.png
├── main.py
├── setup.py
└── README.md
```

- **main.py**: Código principal da aplicação.
- **setup.py**: Script para gerar executável com cx_Freeze.
- **Languages/**: Diretório com opções de idioma e imagens de referência para o reconhecimento do botão.

## Como usar

1. Abra o League of Legends e vá para a tela de busca de partida.
2. Execute o LOL Auto Accept.
3. Selecione o idioma desejado.
4. Clique em "ON" para ativar o auto accept.
5. O programa ficará monitorando a tela. Quando o botão "Aceitar" aparecer, ele será clicado automaticamente.

## Adicionando um novo idioma

1. Crie uma nova pasta dentro de `Languages/` com o nome do idioma.
2. Adicione as imagens `accept.png` e `notaccept.png` referentes ao botão "Aceitar" e ao estado "Não Aceito" nesse idioma.
3. Adicione o idioma à lista em `Languages/Option.txt`.

## Observações

- O programa utiliza reconhecimento de imagem, então as imagens de referência devem ser capturas exatas do botão na sua resolução e idioma.
- Pode ser necessário executar como administrador para que o clique funcione corretamente em alguns sistemas.

## Contribuição

Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de modificar.