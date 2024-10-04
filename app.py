from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_startup_idea(area, problema, publico_alvo):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em startups e inovação."
                },
                {
                    "role": "user",
                    "content": f"Gere uma ideia inovadora de startup considerando:\nÁrea: {area}\nProblema: {problema}\nPúblico-alvo: {publico_alvo}\n\nFormate a resposta com os seguintes tópicos:\n1. Nome sugerido para a startup\n2. Descrição do produto/serviço\n3. Modelo de negócio\n4. Diferencial competitivo\n5. Potencial de mercado"
                }
            ],
            temperature=0.8,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gerar-ideia', methods=['POST'])
def gerar_ideia():
    data = request.json
    area = data.get('area')
    problema = data.get('problema')
    publico_alvo = data.get('publico_alvo')
    
    ideia = generate_startup_idea(area, problema, publico_alvo)
    return jsonify({'ideia': ideia})

if __name__ == '__main__':
    app.run(debug=True)