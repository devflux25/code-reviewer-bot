import streamlit as st
import google.generativeai as genai

genai.configure(api_key="PASTE YOUR API_KEY")

model = genai.GenerativeModel("gemini-2.0-flash")

st.title("Code Reviewer Bot")

st.write("Paste your code below and get instant feedback!")

language = st.selectbox("Select Language",["Python", "C++", "Java", "JavaScript"])

code = st.text_area("Paste your code here",height=250)

col1, col2, col3 = st.columns([2, 2, 5])



with col1:
    review_clicked = st.button("Review My Code")
with col2:
    fix_clicked = st.button("Fix My Code")
with col3:
    explain_clicked = st.button("Explain My Code")

# output displayed here — full width
if review_clicked:
    if code.strip() == "":
        st.warning("Please paste some code first!")
    else:
        with st.spinner("Reviewing your code..."):
            prompt = f"""
            Review this {language} code:
            
            {code}
            
            Give me:
            1. Bugs found
            2. Improvements suggested
            3. Code quality score out of 10
            """
            response = model.generate_content(prompt)
            st.write(response.text)

if fix_clicked:
    if code.strip() == "":
        st.warning("Please paste some code first!")
    else:
        with st.spinner("Fixing your code..."):
            fix_prompt = f"Fix this {language} code and return only the corrected code with no explanation: {code}"
            fix_response = model.generate_content(fix_prompt)
            st.code(fix_response.text)  

if explain_clicked:
    if code.strip() == "":
        st.warning("Please paste some code first!")
    else:
        with st.spinner("Explainng Your Code"):
            explain_prompt = f""
            explain_response = model.generate_content(explain_prompt)
            st.code(explain_response.text)


