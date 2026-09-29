# Nova AI Chatbot Web Application

**Internship Project Phase 1 — Task 1**

A responsive chatbot web application built with Python, Flask, HTML, CSS and JavaScript.

## Features
- Attractive responsive homepage/UI
- Chat interface
- User message and chatbot response system
- Python Flask backend integration
- Typing/loading animation
- Chat history using browser localStorage
- Quick question buttons
- Clear chat option
- Mobile-friendly design

## Project Structure

```text
AI_Chatbot_Web_Application/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Run Locally on Windows

1. Install Python 3.
2. Open this folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Create a virtual environment:

```bash
python -m venv venv
```

5. Activate it:

```bash
venv\Scripts\activate
```

6. Install Flask:

```bash
pip install -r requirements.txt
```

7. Run the project:

```bash
python app.py
```

8. Open `http://127.0.0.1:5000` in your browser.

## About AI/API

This version includes a local Python chatbot response engine, so it works without an API key. The `/chat` endpoint is structured so an external AI API can be integrated later.

## GitHub Upload

Do not upload the `venv` folder. Add it to `.gitignore` before pushing.

Recommended repository name:

`ai-chatbot-web-application`

## Internship Submission

Submit the source code, project screenshots, GitHub repository link, live hosted link, and a short project description.
