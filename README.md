<p align="center">
  <img src="promptmyresume-logo.png" width="200" alt="PromptMyResume logo">
</p>

# PromptMyResume

PromptMyResume is a lightweight Streamlit app that helps you revise resume content using OpenAI's GPT-3.5 and convert it into LaTeX format for use in academic CVs or professional portfolios.

---

## Features

- Analyze resume snippets using GPT-3.5 (via LangChain)
- Suggest 3 specific improvements to tone, clarity, or structure
- Rewrite the content in a more professional, confident voice
- Convert rewritten content into LaTeX `\item` format
- Track token usage and model metadata for transparency

---

## Technologies

- Python
- Streamlit
- LangChain
- OpenAI (via `langchain-openai`)
- dotenv for API key management

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/oscaaa8/PromptMyResume.git
cd PromptMyResume
