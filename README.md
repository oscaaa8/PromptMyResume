# PromptMyResume

**PromptMyResume** is a lightweight, LLM-powered resume editing tool built with Streamlit, LangChain, and OpenAI's GPT-3.5.

It helps users revise resume snippets with actionable feedback, rewrites content using a more confident and professional tone, and converts the output into LaTeX-ready format for use in academic or professional CVs.

---

## 🔍 Features

- ✏️ **Critique Mode**  
  Suggests 3 specific improvements to tone, structure, and clarity using GPT-3.5.

- 🔁 **Rewrite Mode**  
  Generates a refined version of your text using a confident, professional tone.

- 📄 **LaTeX Export**  
  Converts the rewritten version into a clean, `\item`-formatted LaTeX block.

- 📊 **Token Usage + Model Display**  
  Includes total tokens used and model name for transparency.

---

## 🧠 Technologies

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-3.5](https://platform.openai.com/)
- Python + `.env` for API key management

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/oscaaa8/PromptMyResume.git
cd PromptMyResume

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Add your API key to a .env file
echo "OPENAI_API_KEY=your-key-here" > .env

# Run the app
streamlit run app.py
