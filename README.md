# Conversor de PDF em Imagem

Este programa Python converte todas as páginas de um arquivo PDF em imagens e salva essas imagens localmente. É uma ferramenta útil para visualizar ou processar cada página do PDF individualmente como uma imagem.

## Funcionalidades

- Converte todas as páginas de um PDF em imagens.
- Salva cada página como uma imagem.
- Exibe as imagens usando o visualizador de imagens padrão do sistema.

## Pré-requisitos

- Python 3.x
- `pip` (gerenciador de pacotes Python)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA>
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   Crie um arquivo `requirements.txt` com o seguinte conteúdo:

   ```
   pdf2image
   pillow
   ```

   E então execute:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Coloque o arquivo PDF que deseja converter no mesmo diretório do script ou ajuste o caminho do `pdf_path` no código.

2. Execute o script:

   ```bash
   python script.py
   ```

   Onde `script.py` é o nome do seu arquivo Python.

   O script converterá todas as páginas do PDF em imagens e as salvará na pasta especificada. Cada página é salva como uma imagem na pasta `imagens` (ou no nome da pasta que você especificar).

   **Observação:** Cada página do PDF é salva como uma imagem inteira. Se você não precisar salvar as imagens localmente, você pode remover a parte do código que salva as imagens e trabalhar com as imagens temporárias armazenadas na variável `pages`.
