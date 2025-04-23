# This will detect section type *resume or snippet)
# Suggest 3 edits
# Optionally rewrite the input

# Loads the API key & Langchain/OpenAI setup
# Create a PromptTemplate to generate critiques
# Uses an LLMChain to run the model and get structured output
# Opetionally rewrite the text
# Wrap in a clean function interface for your UI to call

# 1. Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# 2. venv\Scripts\activate
# 3. pip install langchain python-dotenv
#    pip install langchain-community (newer versions)
#    pip install -U langchain-openai



import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# load openAI API key
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Step 1 - Initialize LLM
llm = ChatOpenAI(
    openai_api_key = openai_key,
    model_name = "gpt-3.5-turbo",
    temperature = 0.41,
)

# Step 2 - Create Prompt Template for Critique

# Prompt Template for Critique
critique_template = PromptTemplate(
    input_variables=["text"],
    template= """
You are a professional resume editor helping students improve their resumes for graduate school or industry positions.

A user submitted this text:
"{text}"

Your tasks:
1. Determine whether the input is a full resume or just a section (e.g. Education, Experience).
2. Identify whether the tone and formatting are better suited for industry or academia.
3. Suggest exactly 3 specific improvements, focusing on:
   - Tone (confident, concise, polished)
   - Clarity (reduce vagueness)
   - Action verbs and quantification

Respond in the following format:

Thanks for the [{Resume or Section}] — this looks like a [{Industry or Academic}] resume!

**Revision Suggestions**:
1. ...
2. ...
3. ...

(If applicable, include one bonus tip for formatting or structure.)
"""
)
# Step 2.5 - Optional Rewrite Prompt + Chain to generate text
rewrite_template = PromptTemplate(
    input_variables=["text"],
    template="""
You are a resume expert. Your job is to improve this resume text by making it:
- Confident and concise
- Rich in action verbs
- Clear and quantifiable where possible
- Be concise, professional, and avoid repeating words.

Original:
"{text}"

Rewrite this content with a professional tone, avoiding repetition and filler words.
Respond ONLY with the rewritten version — do not explain your edits.
""",
)

# Step 3 - Build the chain

# Chain to generate suggestions
critique_chain = critique_template | llm



# Chain for rewrite
rewrite_chain = rewrite_template | llm



# Step 4. Wrapped Functions
def get_critique(text):
    """Returns section type and 3 revision suggestions"""
    result = critique_chain.invoke({"text": text})

    return {
        "content": result.content,
        "model": result.response_metadata.get("model_name"),
        "token_usage": result.response_metadata.get("token_usage")
    }

def rewrite_text(text):
    """Returns the rewritten version of the input"""
    result = rewrite_chain.invoke({"text": text})
    return {
        "content": result.content,
        "model": result.response_metadata.get("model_name"),
        "token_usage": result.response_metadata.get("token_usage")
    }


