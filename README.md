# Documentação: Gerador de Ideias de Startups

## Descrição
Esta aplicação utiliza a API do ChatGPT para gerar conceitos inovadores de startups com base nos inputs dos usuários. A ferramenta permite que os usuários especifiquem a área de atuação, o problema a ser resolvido e o público-alvo, gerando uma proposta detalhada de startup.

## Requisitos do Sistema
- Python 3.7+
- pip (gerenciador de pacotes Python)
- Conta na OpenAI com API key válida

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd gerador-startups
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install flask openai python-dotenv
pip install flask 
pip install openai==0.28
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
OPENAI_API_KEY=sua_chave_api_aqui
```

## Estrutura do Projeto
```
gerador-startups/
├── app.py
├── templates/
│   └── index.html
├── .env
├── requirements.txt
```

## Como Usar

1. Inicie o servidor:
```bash
python app.py
```

2. Acesse a aplicação em seu navegador:
```
http://localhost:5000
```

3. Preencha o formulário com:
   - Área de atuação da startup
   - Problema que deseja resolver
   - Público-alvo do projeto

4. Clique em "Gerar Ideia" e aguarde a resposta

## Funcionalidades

### Interface do Usuário
- Formulário intuitivo para entrada de dados
- Feedback visual durante o processamento
- Exibição formatada da ideia gerada

### Backend
- Integração com a API do ChatGPT
- Processamento assíncrono das requisições
- Tratamento de erros e exceções

### Resposta Gerada
A API retorna uma ideia de startup formatada com:
1. Nome sugerido para a startup
2. Descrição do produto/serviço
3. Modelo de negócio
4. Diferencial competitivo
5. Potencial de mercado

## Personalização

### Modificando o Prompt
Para ajustar o tipo de resposta gerada, você pode modificar o prompt no arquivo `app.py`:
```python
def generate_startup_idea(area, problema, publico_alvo):
    # Modifique o conteúdo da mensagem conforme necessário
    messages=[
        {
            "role": "system",
            "content": "Você é um especialista em startups e inovação."
        },
        {
            "role": "user",
            "content": f"Gere uma ideia inovadora de startup..."
        }
    ]
```

### Ajustando Parâmetros da API
Você pode modificar os parâmetros da API como temperatura e max_tokens para obter diferentes tipos de respostas:
```python
response = openai.ChatCompletion.create(
    # ...
    temperature=0.8,  # Ajuste para mais (mais criativo) ou menos (mais focado)
    max_tokens=1000   # Ajuste o tamanho máximo da resposta
)
```

## Solução de Problemas

### Erros Comuns

1. **API Key Inválida**
   - Verifique se a chave API está corretamente configurada no arquivo `.env`
   - Confirme se a chave tem saldo disponível na sua conta OpenAI

2. **Erro de Conexão**
   - Verifique sua conexão com a internet
   - Confirme se não há bloqueios de firewall

3. **Timeout da API**
   - Aumente o timeout da requisição se necessário
   - Considere implementar um sistema de retry

## Suporte e Contribuição

Para reportar problemas ou sugerir melhorias:
1. Abra uma issue no repositório
2. Descreva detalhadamente o problema ou sugestão
3. Inclua logs de erro se aplicável

## Licença
Este projeto está licenciado sob a MIT License.

