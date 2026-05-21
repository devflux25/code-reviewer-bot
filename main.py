import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Code Reviewer Bot")

st.write("Paste your code below and get instant feedback!")

language = st.selectbox("Select Language",["Python", "C++", "Java", "JavaScript"])

code = st.text_area("Paste your code here",height=250)

col1, col2, col3, col4 = st.columns([1, 1, 1, 3])

with col1:
    review_clicked = st.button("Review My Code")
with col2:
    fix_clicked = st.button("Fix My Code")
with col3:
    explain_clicked = st.button("Explain My Code")

# output tabs
if review_clicked or fix_clicked or explain_clicked:
    tab1, tab2, tab3 = st.tabs(["Review", "Fix", "Explain"])

    with tab1:
        if review_clicked:
            with st.spinner("Reviewing your code..."):
                try:
                    prompt = f"""
                    Review this {language} code in 150 words max:
                    {code}
                    1. Bugs found
                    2. Top 2 improvements
                    3. Score out of 10
                    """
                    response = model.generate_content(prompt)
                    st.write(response.text)
                except Exception:
                    st.error("⚠️ API limit reached. Please try again tomorrow.")
        else:
            st.info("Click 'Review My Code' to see results here.")

    with tab2:
        if fix_clicked:
            with st.spinner("Fixing your code..."):
                try:
                    fix_prompt = f"Fix this {language} code and return only corrected code with no explanation: {code}"
                    fix_response = model.generate_content(fix_prompt)
                    st.code(fix_response.text)
                except Exception:
                    st.error("⚠️ API limit reached. Please try again tomorrow.")
        else:
            st.info("Click 'Fix My Code' to see results here.")

    with tab3:
        if explain_clicked:
            with st.spinner("Explaining your code..."):
                try:
                    explain_prompt = f"Explain this {language} code line by line in simple English for a beginner: {code}"
                    explain_response = model.generate_content(explain_prompt)
                    st.write(explain_response.text)
                except Exception:
                    st.error("⚠️ API limit reached. Please try again tomorrow.")
        else:
            st.info("Click 'Explain My Code' to see results here.")

