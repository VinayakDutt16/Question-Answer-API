# Added additional comments to explain code methods
# Import necessary modules
from flask import Flask, request, render_template, jsonify
import openai

# Create a Flask application instance
app = Flask(__name__)

# Set OpenAI API key 
OPENAI_API_KEY = ""

# Set OpenAI API key in the openai module
openai.api_key = OPENAI_API_KEY

# Route to render the main HTML page
@app.route('/')
def index():
    # Render the main HTML page
    return render_template('index.html')

# API endpoint to handle POST requests and get answers
@app.route('/get_answer', methods=['POST'])
def get_answer():
    try:
        # Check if the request has a JSON payload
        if not request.is_json:
            # Return an error response if JSON payload is not present
            return jsonify({"error": "Invalid request. JSON payload required."}), 400

        # Parse the JSON payload
        data = request.json

        # Check if the request contains the 'question' key
        if 'question' not in data:
            # Return an error response if 'question' key is not found
            return jsonify({"error": "Invalid request. 'question' key not found."}), 400

        # Extract the question from the JSON payload
        question = data['question']

        # Use OpenAI Chat API to get the response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )

        # Extract the answer from the OpenAI API response
        answer = response['choices'][0]['message']['content']

        # Format the response
        response_data = {"question": question, "answer": answer}

        # Return the formatted response as JSON
        return jsonify(response_data)

    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
