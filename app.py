from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

OPENAI_API_KEY = ""
openai.api_key = OPENAI_API_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_answer', methods=['POST'])
def get_answer():
    try:
        if not request.is_json:
            return jsonify({"error": "Invalid request. JSON payload required."}), 400

        data = request.json

        if 'question' not in data:
            return jsonify({"error": "Invalid request. 'question' key not found."}), 400

        question = data['question']

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )

        answer = response['choices'][0]['message']['content']

        response_data = {"question": question, "answer": answer}
        return jsonify(response_data)

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
