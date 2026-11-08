# SolveIt - AI Problem Solver

A simple AI chatbot that gives short, clear answers to everyday, study, and general problems. It replies in Roman Urdu and keeps the conversation going, so you can ask follow-up questions.

**Live app:** [add your Streamlit link here]

## Features

- Chat interface with conversation memory
- Short, direct answers (no long tables or extra text unless you ask for "poora samjhao")
- Replies in Roman Urdu
- Friendly error message if the AI service is unavailable

## Tech Stack

- Python
- [Streamlit](https://streamlit.io) for the web interface
- [Groq API](https://console.groq.com) for the AI model (`openai/gpt-oss-120b`)

## Project Structure

```
SolveIt/
├── app.py              # The chatbot app
├── requirements.txt    # Python libraries needed
├── .gitignore          # Keeps secret keys out of GitHub
└── README.md           # This file
```

## Run It Locally

1. Clone the repository and open the folder.
2. Install the libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a file `.streamlit/secrets.toml` and add your Groq API key:
   ```toml
   GROQ_API_KEY = "your_key_here"
   ```
4. Start the app:
   ```bash
   streamlit run app.py
   ```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app**, choose the `SolveIt` repository, and set the main file to `app.py`.
4. Under **Advanced settings → Secrets**, add:
   ```toml
   GROQ_API_KEY = "your_key_here"
   ```
5. Click **Deploy**.

## Important Notes

- Never commit your API key to GitHub. Keep it only in Streamlit Secrets or in the local `secrets.toml` file (which is listed in `.gitignore`).
- AI answers can be wrong. Please double-check important answers, especially for math, science, health, or legal questions.
- Model names on Groq change from time to time. If you get a "model not found" error, update the `MODEL` value in `app.py` with a current model name from the Groq docs.

## Author

Made by [Your Name]
