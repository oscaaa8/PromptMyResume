# Accepts raw or rewritten text
# Converts to LaTeX format with section/line detection

def convert_to_latex(text: str, section_title: str = "Experience") -> str:
    """
    Converts rewritten resume text into LaTeX bullet point format.
    Default section is 'Experience', but can be changed.
    """
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    latex_items = ""
    for line in lines:
        latex_items += f"  \\item {line}\n"

    latex_output = f"""\\section*{{{section_title}}}
\\begin{{itemize}}
{latex_items}\\end{{itemize}}
"""
    return latex_output
