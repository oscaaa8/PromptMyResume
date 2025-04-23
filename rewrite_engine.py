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
You are a professional resume editor designed to help students craft graduate-school ready CVs and Resumes. 
A user has submitted this text:

"{text}"

First, determine: is this a full resume, or just a section?
Then, suggest 3 specific improvements that could be made (focus on tone, clarifty, action verbs, quantification)
and any other relevant details to edit for a successful grad school or industry ready resume/cv. 

Respond in this format:
Thanks for the [Resume/Snippet] Looks like you are trying to write a (industry-ready/grad-school ready) resume!

Revision Suggestions:
1. ...
2. ...
3. ...
"""
)
# Step 2.5 - Optional Rewrite Prompt + Chain to generate text
rewrite_template = PromptTemplate(
    input_variables=["text"],
    template="""
You are a resume expert. Improve this text using confident tone, strong action verbs, and clarity.
Be concise, professional, and avoid repeating words.

Rewrite:
"{text}"

Respond with only the rewritten version.
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


