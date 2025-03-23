# Teste Automatizado do Controller para Cadastro de Profissionais.

Este repositório contém um teste automatizado para o endpoint de criação de profissionais da API Cloudify.

## Teste realizado por: 
Tainá de Paiva Cortez 

## Teste relacionado ao projeto:
Cloudify - G02 - Engenharia de Software

## Caso de Teste: Criação de Profissional

### Objetivo
Verificar se o endpoint de criação de profissionais está funcionando corretamente, aceitando os parâmetros e retornando os dados do profissional quando criado.

### Pré-condição
- A API deve estar em execução na URL configurada
- O banco de dados deve estar disponível
- A tabela PROFESSIONALS deve estar criada no banco de dados

### Procedimento de Teste
1. Preparar os dados de um novo profissional (nome, email, celular e número)
2. Enviar uma requisição POST para o endpoint `/professionals` com os dados do profissional
3. Verificar se o status code da resposta é 201 (Created)
4. Verificar se a resposta contém os dados do profissional criado, incluindo um ID

### Resultado Esperado
- Status code: 201
- Resposta: JSON contendo os dados do profissional criado, incluindo um ID gerado pelo sistema
- Todos os campos enviados na requisição devem estar presentes na resposta com os mesmos valores

### Resultado Obtido
- Status code: 201 (Created)
- Resposta: JSON contendo os dados do profissional criado, incluindo:
  ```json
  {
    "id": 6,
    "name": "Tainá Cortez",
    "email": "corteztaina23@gmail.com",
    "cellphone": "12996855262",
    "number": "121212"
  }

- Logs: O sistema registrou no console a mensagem "Profissional criado com sucesso" seguida dos detalhes do profissional.
### Pós-condição
Um novo registro de profissional é criado no banco de dados com os dados fornecidos.

## Como executar o teste

1. Certifique-se de que a API está em execução
2. Instale as dependências:
- pip install -r requirements.txt
3. Execute o teste:
- python test_professional_api.py