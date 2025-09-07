# Smart India Hackathon – Chatbot Project

## 📌 Overview
This project was developed as part of the **Smart India Hackathon (SIH)**.  
It is a **rule-based chatbot** built using the **RASA framework**, integrated with a **Flask backend** and a simple HTML interface.  
The chatbot handles **structured queries and FAQs**, providing deterministic responses based on predefined intents and rules.

---

## ⚡ Features
- Rule-based chatbot with **intents and entities** defined in YAML files.
- **Custom Python actions** for handling domain-specific queries.
- **RASA NLU** for intent classification and response mapping.
- Flask integration for backend support.
- Simple **HTML frontend** for interaction.

---

## 🛠️ Tech Stack
- **Languages:** Python, HTML, YAML  
- **Frameworks/Tools:** RASA, Flask  
- **Libraries:** RASA NLU, RASA Core  
- **Other:** Rule-based NLP, YAML configuration  

---

## 🚀 Setup Instructions
1. Clone this repository:
   git clone https://github.com/your-username/Smart_India_Hackathon.git
   cd Smart_India_Hackathon
2. Install dependencies:
    pip install rasa flask
3. Train the chatbot:
    rasa train
4. Run the chatbot server:
    rasa run actions
    rasa shell
5. Start the Flask app for the frontend:
    python app.py
