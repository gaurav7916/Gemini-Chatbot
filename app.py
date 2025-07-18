from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import os

app = Flask(__name__)
api_key = os.getenv('AIzaSyBN4UzuZC2e6-NvoRKn0tw5a_xgE4l0ykU')

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

# Define your 404 error handler to redirect to the index page
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        try:
            response = model.generate_content(prompt)
            # Check if response is valid and contains the expected parts
            if hasattr(response, 'text') and response.text:
                return response.text
            else:
                return "Gemini returned an unexpected response format."
            
        except Exception as e:
            return f"An error occurred while processing the request: {str(e)}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
