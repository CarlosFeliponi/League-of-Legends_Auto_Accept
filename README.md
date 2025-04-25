# League of Legends Auto Accept

League of Legends Auto Accept is an automated tool to quickly and efficiently accept matches in League of Legends. Using image recognition, the program detects the "Accept" button on the screen and clicks it automatically, so you don't miss matches by failing to accept in time.

---

## Features

- **Automatic match acceptance:** Detects and clicks the "Accept" button as soon as it appears.
- **Simple graphical interface:** Choose the language and easily enable/disable auto accept.
- **Multi-language support:** Currently supports Portuguese and English (easily extensible).
- **Cross-platform code:** Main functionality works on any OS, but executable generation is configured for Windows (via cx_Freeze).
- **Easy to add new languages:** Just add a folder and images.

---

## Installation

### Prerequisites

- Python 3.7+
- pip

### Dependencies

Install all dependencies with:

```
pip install -r requirements.txt
```

If you prefer, you can install manually:

```
pip install pyautogui opencv-python numpy tk
```

On Windows, `cx_Freeze` will also be installed if you use the requirements file.

---

The executable will be in the `build` folder.

---

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
├── requirements.txt
├── .gitignore
└── README.md
```

- **main.py**: Main application code and GUI.
- **setup.py**: Script to generate executable with cx_Freeze.
- **requirements.txt**: List of required Python packages.
- **Languages/**: Directory with language options and reference images for button recognition.

---

## How to Use

1. Open League of Legends and go to the match search screen.
2. Run LOL Auto Accept (`python main.py` or the generated executable).
3. Select the desired language.
4. Click "ON" to activate auto accept.
5. The program will monitor the screen. When the "Accept" button appears, it will be clicked automatically.

---

## Adding a New Language

1. Create a new folder inside `Languages/` with the name of the language.
2. Add `accept.png` and `notaccept.png` images for the "Accept" button and the "Not Accepted" state in that language.
3. Add the language to the list in `Languages/Option.txt`.

---

## Notes

- The program uses image recognition, so the reference images must be exact screenshots of the button in your resolution and language.
- You may need to run as administrator for the click to work properly on some systems.
- If you change the language while auto accept is ON, the change will only take effect the next time you activate auto accept.

---

## Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

# League of Legends Auto Accept (Português)

League of Legends Auto Accept é uma ferramenta automatizada para aceitar partidas no League of Legends de forma rápida e eficiente. Utilizando reconhecimento de imagem, o programa detecta o botão "Aceitar" na tela e clica automaticamente, evitando que você perca partidas por não aceitar a tempo.

---

## Funcionalidades

- **Aceitação automática de partidas:** Detecta e clica no botão "Aceitar" assim que ele aparece.
- **Interface gráfica simples:** Escolha o idioma e ative/desative o auto accept facilmente.
- **Suporte a múltiplos idiomas:** Atualmente suporta Português e Inglês (fácil de expandir).
- **Código multiplataforma:** Funciona em qualquer sistema operacional, mas a geração do executável está configurada para Windows (via cx_Freeze).
- **Fácil de adicionar novos idiomas:** Basta adicionar uma pasta e imagens.

---

## Instalação

### Pré-requisitos

- Python 3.7+
- pip

### Dependências

Instale todas as dependências com:

```
pip install -r requirements.txt
```

Ou, se preferir, instale manualmente:

```
pip install pyautogui opencv-python numpy tk
```

No Windows, o `cx_Freeze` também será instalado se você usar o arquivo de requisitos.

---

## Executando via código-fonte

1. Clone o repositório:
    ```
    git clone https://github.com/CarlosFeliponi/League-of-Legends_Auto_Accept.git
    cd League-of-Legends_Auto_Accept
    ```

2. Execute o programa:
    ```
    python main.py
    ```

---

## Gerando Executável (Windows)

1. Instale o cx_Freeze (se ainda não estiver instalado):
    ```
    pip install cx_Freeze
    ```

2. Gere o executável:
    ```
    python setup.py build
    ```

O executável estará na pasta `build`.

---

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
├── requirements.txt
├── .gitignore
└── README.md
```

- **main.py**: Código principal da aplicação e interface gráfica.
- **setup.py**: Script para gerar executável com cx_Freeze.
- **requirements.txt**: Lista de pacotes Python necessários.
- **Languages/**: Diretório com opções de idioma e imagens de referência para o reconhecimento do botão.

---

## Como usar

1. Abra o League of Legends e vá para a tela de busca de partida.
2. Execute o LOL Auto Accept (`python main.py` ou o executável gerado).
3. Selecione o idioma desejado.
4. Clique em "ON" para ativar o auto accept.
5. O programa ficará monitorando a tela. Quando o botão "Aceitar" aparecer, ele será clicado automaticamente.

---

## Adicionando um novo idioma

1. Crie uma nova pasta dentro de `Languages/` com o nome do idioma.
2. Adicione as imagens `accept.png` e `notaccept.png` referentes ao botão "Aceitar" e ao estado "Não Aceito" nesse idioma.
3. Adicione o idioma à lista em `Languages/Option.txt`.

---

## Observações

- O programa utiliza reconhecimento de imagem, então as imagens de referência devem ser capturas exatas do botão na sua resolução e idioma.
- Pode ser necessário executar como administrador para que o clique funcione corretamente em alguns sistemas.
- Se você mudar o idioma enquanto o auto accept está ON, a mudança só terá efeito na próxima vez que ativar o auto accept.

---

## Contribuição

Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de modificar.