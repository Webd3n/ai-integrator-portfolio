
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'ТУК_ПОСТАВИ_СВОЯ_API_КЛЮЧ'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}],
        max_tokens=150
    )

    answer = response['choices'][0]['message']['content']
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
