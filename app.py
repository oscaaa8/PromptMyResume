"""
Goal:
- Split screen layout windowed (left = input , right = output)
- Button function for revise
- Button function for Convert to LaTex

Output Area:
- Rewritten content
- Token Usage
- Model Name
"""
# pip install streamlit

import streamlit as st
from rewrite_engine import get_critique, rewrite_text
from latex_converter import convert_to_latex


st.set_page_config(page_title="Resume Refiner", layout = "wide")

# UI TITLE
st.title("Refine Your Resume")
st.markdown("Paste your resume or a section below. Choose to either revise the content or convert it to LaTeX.")


# SPLIT LAYOUT
left_col, right_col = st.columns(2)

# LEFT: USER INPUT
with left_col:
    st.markdown("### Your Resume or Snippet")
    user_input = st.text_area("Paste resume content here:", height = 300)

    col1, col2 = st.columns(2)
    with col1:
        revise_clicked = st.button("Revise")
    with col2:
        latex_clicked = st.button("Convert to LaTeX")


# =================== RIGHT: OUTPUT ===================
with right_col:
    st.markdown("### Output")

    if revise_clicked and user_input.strip():
        with st.spinner("Analyzing..."):
            critique = get_critique(user_input)
            rewrite = rewrite_text(user_input)

        st.markdown("---")
        st.markdown("#### Critique Suggestions")
        st.write(critique["content"])

        st.markdown("---")
        st.markdown("#### Rewritten Version")
        st.markdown(f'<div class="highlight-box">{rewrite["content"]}</div>', unsafe_allow_html=True)

        st.markdown("---")
        st.markdown(f"**Model Used:** `{rewrite['model']}`")
        st.markdown(f"**Tokens Used:** Prompt `{rewrite['token_usage']['prompt_tokens']}` + Completion `{rewrite['token_usage']['completion_tokens']}` = Total `{rewrite['token_usage']['total_tokens']}`")

    elif latex_clicked and user_input.strip():
        with st.spinner("Converting to LaTeX..."):
            rewrite = rewrite_text(user_input)
            latex_code = convert_to_latex(rewrite["content"], section_title="Experience")

            st.markdown("### LaTeX Output")
            st.code(latex_code, language = "latex")
            