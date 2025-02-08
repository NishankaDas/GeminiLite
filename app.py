from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Configure your Gemini API Key
genai.configure(api_key="AIzaSyCMekqEIs-lmHevESdWrV3ghm56D2_kltX")

# Function to get response from Gemini
def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return "Error: Unable to process the request."

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    bot_response = get_gemini_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
