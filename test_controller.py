import requests
import json
import unittest

class TestProfessionalAPI(unittest.TestCase):
    # URL base da sua API (ajuste conforme necessário)
    BASE_URL = "http://localhost:3000"
    
    def setUp(self):
        # Configuração que será executada antes de cada teste
        self.endpoint = f"{self.BASE_URL}/professionals"
        self.headers = {"Content-Type": "application/json"}
        
        # Dados de teste para um novo profissional
        self.test_professional = {
            "name": "Teste Automatizado",
            "email": "teste@automatizado.com",
            "cellphone": "11999998888",
            "number": "123"
        }
    
    def test_create_professional(self):
        """
        Teste para verificar se a API cria um profissional corretamente
        """
        # Fazendo a requisição POST para criar um novo profissional
        response = requests.post(
            self.endpoint,
            headers=self.headers,
            data=json.dumps(self.test_professional)
        )
        
        # Verificando se o status code é 201 (Created)
        self.assertEqual(response.status_code, 201, f"Falha ao criar profissional: {response.text}")
        
        # Verificando se o response contém os dados corretos
        data = response.json()
        self.assertIn("id", data, "Resposta não contém ID do profissional")
        self.assertEqual(data["name"], self.test_professional["name"], "Nome do profissional não corresponde")
        self.assertEqual(data["email"], self.test_professional["email"], "Email do profissional não corresponde")
        self.assertEqual(data["cellphone"], self.test_professional["cellphone"], "Celular do profissional não corresponde")
        self.assertEqual(data["number"], self.test_professional["number"], "Número do profissional não corresponde")
        
        print(f"Profissional criado com sucesso! ID: {data['id']}")
        
        # Poderia adicionar uma limpeza aqui para deletar o profissional criado
        # mas isso dependeria de um endpoint de deleção estar implementado

if __name__ == "__main__":
    unittest.main()