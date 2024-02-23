# Question-Answer-API
This project implements a RESTful API that interacts with OpenAI's Chat API to provide answers to user questions. The API is built using the Flask web framework in Python and display the results in JSON format.

Question Answer API Implementation Report
Summary:
This project implements a Flask-based RESTful API interacting with the OpenAI API to answer user questions. The API receives questions via HTTP POST requests, sends them to the OpenAI API, and returns formatted responses.

## Key Components:
### installation requirements:

**pip install Flask requests**

**pip install openai==0.28**

Flask Application (app.py):

Implements a Flask web application.
Imports necessary modules (Flask, request, render_template, jsonify, openai), creates a Flask application instance.

## OpenAI Configuration:

Initializes an OpenAI API key (replace the empty string with the actual key), sets the OpenAI API key in the openai module.

## Routes:

Defines a route ("/") that renders the main HTML page.
GET Request Handler:

Displays the main HTML page when the root URL is accessed.
POST Request Handler:

Handles POST requests to "/get_answer".
Validates if the request has a JSON payload and if it contains the 'question' key.
Uses OpenAI Chat API to get a response based on the user's question.
Parses the response and formats it as a JSON containing the question and its answer.
Returns the formatted response.
Main Execution:

Runs the Flask application in debug mode.

to run the flask app -> **python app.py**

Utilizes the OpenAI Chat API for answering questions.

Renders an HTML form for user interaction.

## HTML User Interface (index.html):

### HTML Structure:

Basic HTML structure with a form to input a question and display the response.

### Styles:

Simple styles for the page layout.

### Form:

A form with a text input for the question and a button to submit.

### Response Display:

A section to display the response, with separate areas for the question and answer.

### JavaScript:

Listens for the form submission event.
Prevents the default form submission behavior.
Fetches the answer from the server using a POST request.
Updates the displayed question and answer based on the server's response

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
