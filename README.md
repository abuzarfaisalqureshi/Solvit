 # SolveIt

SolveIt ek simple AI chatbot hai jo roz-marra, parhai aur general problems ke chhote aur seedhe jawab deta hai. Jawab Roman Urdu mein aate hain aur chatbot pichli baat yaad rakhta hai, isliye follow-up sawal bhi poochh sakte ho.

## Features

- Chat interface jisme baat-cheet yaad rehti hai
- Chhote aur seedhe jawab (detail sirf tab jab "poora samjhao" likho)
- Roman Urdu mein jawab
- AI service band ho to saaf error message

## Tech Stack

- Python
- Streamlit (website ke liye)
- Groq API (AI model: `openai/gpt-oss-120b`)

## Files

- `app.py`: chatbot ka code
- `requirements.txt`: zaroori libraries
- `.gitignore`: secret key ko GitHub se bachata hai

## Deploy kaise karein (Streamlit Community Cloud)

1. Repository GitHub par upload karo.
2. share.streamlit.io par GitHub se login karo.
3. **Create app** dabao, repository `SolveIt` chuno, main file `app.py` rakho.
4. **Advanced settings** mein **Secrets** mein ye likho:
   ```toml
   GROQ_API_KEY = "yahan_apni_key"
   ```
5. **Deploy** dabao.

## Zaroori baatein

- API key kabhi GitHub par mat daalo. Sirf Streamlit Secrets mein rakho.
- AI ke jawab ghalat bhi ho sakte hain. Math, science, sehat ya qanooni sawalon ke jawab khud check karo.
- Groq kabhi kabhi models ke naam badal deta hai. Agar "model not found" error aaye to `app.py` mein `MODEL` ka naam current naam se badal do.
