# Question-Answer-API
This project implements a RESTful API that interacts with OpenAI's Chat API to provide answers to user questions. The API is built using the Flask web framework in Python and display the results in JSON format.

Question Answer API Implementation Report
Summary:
This project implements a Flask-based RESTful API interacting with the OpenAI API to answer user questions. The API receives questions via HTTP POST requests, sends them to the OpenAI API, and returns formatted responses.

## Key Components:
Flask Application (app.py):

Implements a Flask web application.

Utilizes the OpenAI Chat API for answering questions.

Renders an HTML form for user interaction.

## HTML User Interface (index.html):

Provides a simple and responsive user interface.

Accepts user questions via a form.

Displays questions and answers in a well-formatted manner.

# Features:

## API Endpoint Creation:

RESTful API endpoint at /get_answer.

Accepts HTTP POST requests with JSON payload containing a question.

## Integration with OpenAI API:

Interacts with OpenAI Chat API.
Forwards user questions and retrieves responses.

## Response Handling:

Parses and formats responses from the OpenAI API.
Formats responses in a structured manner: {"question": "...", "answer": "..."}.

## Error Handling:

Gracefully handles errors for invalid requests.
Provides clear error messages and appropriate HTTP status codes.
Ensures robustness in communication with the OpenAI API.
