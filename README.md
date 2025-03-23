# Teste Automatizado do Controller para Cadastro de Profissionais.

Este repositório contém um teste automatizado para o endpoint de criação de profissionais da API Cloudify.

## Caso de Teste: Criação de Profissional

### Objetivo
Verificar se o endpoint de criação de profissionais está funcionando corretamente, aceitando os parâmetros necessários e retornando os dados do profissional criado com status code 201.

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
*Será documentado após a execução do teste*

### Pós-condição
Um novo registro de profissional é criado no banco de dados com os dados fornecidos.

## Como executar o teste

1. Certifique-se de que a API está em execução
2. Instale as dependências: