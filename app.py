import streamlit as st
from groq import Groq

st.set_page_config(page_title="SolveIt", page_icon="💡")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODEL = "openai/gpt-oss-120b"

SYSTEM_PROMPT = """Tum ek helpful assistant ho. Jawab seedha aur clear do.
Rules:
- Jawab ek chhote paragraph (3-4 lines) mein do.
- Table, headings, bullet points ya lambi calculation mat likho.
- Math ho to sirf zaroori kaam ek do line mein likho, phir final answer.
- Roman Urdu mein jawab do.
- Practice questions ya extra baatein tab hi do jab user maange.
- Detail sirf tab do jab user "poora samjhao" kahe."""

st.title("SolveIt - Problem Solver")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chat screen par dikhao
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# Naya sawal lo
if prompt := st.chat_input("Apni problem likho"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "system", "content": SYSTEM_PROMPT}]
                + st.session_state.messages,
            )
            reply = response.choices[0].message.content
        except Exception:
            reply = "Kuch masla aa gaya, dobara try karo."
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

# ---------- Sidebar: History (file ke aakhir mein hi rehne do) ----------
with st.sidebar:
    st.header("History")

    questions = [m["content"] for m in st.session_state.messages if m["role"] == "user"]
    if questions:
        for i, q in enumerate(questions, 1):
            st.write(f"{i}. {q[:60]}")
    else:
        st.caption("Abhi koi sawal nahi poochha.")

    if st.button("Nayi chat"):
        st.session_state.messages = []
        st.rerun()

    if st.session_state.messages:
        chat_text = "\n\n".join(
            f"{'Tum' if m['role'] == 'user' else 'SolveIt'}: {m['content']}"
            for m in st.session_state.messages
        )
        st.download_button("Chat download karo", chat_text, file_name="solveit_chat.txt")
