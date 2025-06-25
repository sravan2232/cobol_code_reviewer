import streamlit as st
from pathlib import Path
from parsers.cobol_parsers import parse_cobol_code
from models.ai_analyzer import ask_local_ai

st.set_page_config(page_title="COBOL Code Reviewer", layout="wide")
st.title("🔍 AI-powered COBOL Code Reviewer")

uploaded_file = st.file_uploader("Upload your COBOL/JCL file", type=["cbl", "jcl", "txt"])

if uploaded_file:
    file_contents = uploaded_file.read().decode("utf-8")
    st.subheader("📄 Uploaded Code Preview")
    st.code(file_contents, language="cobol")

    if st.button("🔍 Analyze Code with AI"):
        parsed = parse_cobol_code(file_contents)

        st.subheader("📌 Parsed Sections")
        for key in ["IDENTIFICATION DIVISION", "ENVIRONMENT DIVISION", "DATA DIVISION", "PROCEDURE DIVISION"]:
            if parsed[key]:
                st.markdown(f"### 🔹 {key}")
                st.code(parsed[key])

        st.subheader("🧠 AI Explanation (Procedure Division)")
        explanation = ask_ai(
            f"Explain the following COBOL PROCEDURE DIVISION in simple terms for a junior developer:\n\n{parsed['PROCEDURE DIVISION']}"
        )
        st.write(explanation)

        st.subheader("🔍 Code Insights")
        st.markdown(f"**File Operations**: {', '.join(parsed['FILE OPERATIONS']) or 'None'}")
        st.markdown(f"**PERFORM Blocks**: {', '.join(parsed['PERFORM BLOCKS']) or 'None'}")
        st.markdown(f"**GOTO Usage**: {', '.join(parsed['GOTO USAGE']) or 'None'}")
