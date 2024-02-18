from flask import Flask, render_template, request, jsonify
import requests

RASA_API_URL = 'http://0.0.0.0:5005/webhooks/rest/webhook'  # Replace with your Rasa API URL

app = Flask(__name__,template_folder="template")

@app.route('/')
def index():
    return render_template('index1.html')  # You can create an HTML template for your chat interface

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)

    # Send the user message to the Rasa API
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response: ", rasa_response_json)

    bot_response = rasa_response_json[0]['text']
    print('bot:', bot_response)

    if rasa_response_json :
        return jsonify({'response': bot_response})
    else :
        print('Sorry')


if __name__ == "__main__":
   app.run(debug=True, port=5000)


