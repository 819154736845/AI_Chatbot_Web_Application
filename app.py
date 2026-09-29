from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)


def chatbot_response(message):
    text = message.lower().strip()
    if not text:
        return "Please type a message so I can help you."
    if any(x in text for x in ["hello", "hi", "hey", "hii"]):
        return "Hello! 👋 I'm Nova, your AI-style assistant. How can I help you today?"
    if "your name" in text or "who are you" in text:
        return "I'm Nova, a chatbot built with Python Flask, HTML, CSS and JavaScript."
    if "python" in text:
        return "Python is a beginner-friendly programming language used in web development, automation, data science, AI and machine learning."
    if "flask" in text:
        return "Flask is a lightweight Python web framework used for building web applications and APIs."
    if "html" in text:
        return "HTML creates the structure of a web page. CSS controls its design, while JavaScript adds interactivity."
    if "css" in text:
        return "CSS is used to style web pages, including colors, spacing, layouts, animations and responsive designs."
    if "javascript" in text or " js" in text:
        return "JavaScript makes web pages interactive. In this project it sends messages to the Flask backend without reloading the page."
    if "internship" in text:
        return "This project demonstrates frontend design, JavaScript interaction and Python Flask backend integration."
    if "time" in text:
        return f"The server time is {datetime.now().strftime('%I:%M %p')}."
    if any(x in text for x in ["thank", "thanks"]):
        return "You're welcome! 😊 Keep learning and building projects."
    return "That's an interesting question! I'm currently running in demo mode. You can ask me about Python, Flask, HTML, CSS, JavaScript or web development."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    return jsonify({"reply": chatbot_response(data.get("message", ""))})


if __name__ == "__main__":
    app.run(debug=True)
