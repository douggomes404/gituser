# GitHub User Report Generator

Este projeto é um script Python que utiliza a API do GitHub para obter informações de um usuário e gerar um relatório com essas informações. O relatório é salvo em um arquivo de texto no diretório de relatórios.

## Funcionalidades

- Solicita ao usuário que insira o nome de usuário do GitHub.
- Obtém os dados do usuário usando a API do GitHub.
- Gera um relatório contendo informações sobre o usuário e seus repositórios públicos.
- Salva o relatório em um arquivo de texto no diretório de relatórios.

## Como Usar

1. Instale as bibliotecas necessárias:

`pip install -r requirements.txt `

2. Execute o script main.py:
` python main.py `

3. Insira o nome de usuário do GitHub quando solicitado.

4. O relatório será gerado e salvo no diretório `./relatorio/.`

5. Certifique-se de ajustar as configurações do projeto conforme necessário para atender às suas preferências e requisitos.

## Estrutura de Diretórios

gituser/
│
├── main.py
│
└── modules/
    │
    ├── github_api.py
    │
    ├── report_generator.py
    │
    └── app.py

`main.py:` Arquivo que inicia o programa chamando app.py.
`modules/github_api.py:` Classe que encapsula a função para obter dados do usuário do GitHub.
`modules/report_generator.py:` Classe que gera o relatório do usuário.
`modules/app.py:` Classe que inicia o programa, controlando o fluxo e interações.

## Personalização

Você pode ajustar o diretório onde os relatórios são salvos no arquivo `app.py`.

Você também pode modificar o nome das pastas ou arquivos conforme necessário.

Este é um projeto básico e pode ser expandido com mais recursos e funcionalidades, como a obtenção de informações adicionais dos repositórios, tratamento de erros mais detalhado, entre outros.

Lembre-se de substituir seu-usuario no URL do repositório pelo seu nome de usuário do GitHub e de ajustar as informações e detalhes do projeto de acordo com suas necessidades.