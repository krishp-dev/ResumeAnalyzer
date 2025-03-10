import streamlit as st
import google.generativeai as genai
import os 
import PyPDF2 as pdf

import time
from dotenv import load_dotenv
# from docx import Document
load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_resopnse(input):
    time.sleep(2)
    model = genai.GenerativeModel('gemini-1.5-pro')
    resopnse = model.generate_content(input) 
    return resopnse.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

def prompt1(text,jd):
    prompt = f"""
    Hey act like ATS(Application Tracking System) with deep understanding of tech field, software engineering ,data science, data analyst , big data engineer and for other tech job related to software part . your task is to evaluate the resume based on the given job description . you must consider the job market is very competitive and you should provie best assistance for improving the resume. assign the percentage matching based on job description 
    resume:{text}
    description:{jd}

    i want the resopnse like :
    Job Matching : 40%(according to ur evaluation)

    don't anythinh else just respond Job Matching in percentage.

    """
    return prompt

def prompt2(text,jd):
    prompt = f"""
    Hey act like ATS(Application Tracking System) with deep understanding of tech field, software engineering ,data science, data analyst , big data engineer and for other tech job related to software part . your task is to evaluate the resume based on the given job description . you must consider the job market is very competitive and you should provie best assistance for improving the resume. give me keywords that are missing and can immporve my resume with high accuracy.

    resume:{text}
    job description:{jd}

    i want the resopnse like :
    1.keyword1
    2.keyword2
    .
    .

    don't anything else just respond Missing Keywords then mention the keywords according to job description with high accuracy.
    make sure that keywords should relate to job description in some way.
    """
    return prompt

def prompt3(text):
    prompt = f"""
            Hey act like ATS(Application Tracking System) with deep understanding of tech field, software engineering ,data science, data analyst , big data engineer and for other tech job related to software part . your task is to generate summary of give resume. highlighting weakness and strength as bullet points after summary.

            resume:{text}

            i want the resopnse like :
            personal details(must be in bullet points)
            Name:
            Email:
            PhoneNo: 
            summary...\n
            Strength:
            points\n
            Weakness:
            points\n
            weakness and strength points must not more than 8 words.
            """
    return prompt

def prompt4(text,jd):
    prompt = f"""
    Hey act like ATS(Application Tracking System) with deep understanding of tech field, software engineering ,data science, data analyst , big data engineer and for other tech job related to software part . your task is to evaluate to check grammatical mistakes and resume format . you must consider the job market is very competitive and you should provie best assistance for improving the resume based on job description 

    resume:{text}
    description:{jd}

    i want the resopnse like :
    list the grammatical mistakes and help improve to resume with grammar and with format if needed

    just respond like it is mentioned above don't or change anything according to yourself and don't give any description or explaination about anything  other than the grammatical mistakes and format. only string response
    """
    return prompt

def prompt5(text):
    prompt = f"""
    Act as an advanced ATS (Applicant Tracking System) with a deep understanding of the tech industry, including software engineering, data science, data analytics, big data engineering, and other software-related roles. Assume a highly competitive job market and provide the best assistance.

    Your task is to evaluate the resume based on work experience, projects, and skills, then predict the most likely job positions the applicant can get.

    Resume:
    {text}

    Response Format:

    Job Position: Percentage chance of getting the job\n
    Job Position: Percentage chance of getting the job\n
    (Continue in this format, one per line, without explanations or extra text)
    Do not add descriptions, explanations, or anything beyond the required format. Respond strictly as instructed.
    """
    return prompt

def prompt6(text):
    prompt = f"""
    Hey act like ATS(Application Tracking System) with deep understanding of tech field, software engineering ,data science, data analyst , big data engineer and for other tech job related to software part . your task is to evaluate the details based on that generate resume. you must consider the job market is very competitive and you should provie best assistance for improving the resume.
    
    details:{text}

    i want the resopnse like :
    (resume in text)

    don't do anything else just generate the resume as per details and should highly professional.with simple words

    """
    return prompt

def prompt7(text):
    prompt = f"""
        Hey act like ATS(Application Tracking System) with deep understanding of tech field, software engineering ,data science, data analyst , big data engineer and for other tech job related to software part . your task is to evaluate the cover letter based on the given job description . you must consider the job market is very competitive and you should provie best assistance for improving the cover letter. 

        cover letter:{text}

        i want the resopnse like :
        Cover Letter Score:(out of 10)
        
        Mistakes:
        (bullet points)

        don't do anythinh else just respond score and mistakes and make sure mistakes explained should be short.
        If its not cover letter respond that please enter cover letter.
    """
    return prompt

def prompt8(text):
    prompt = f"""
        Hey act like ATS(Application Tracking System) with deep understanding of tech field, software engineering ,data science, data analyst , big data engineer and for other tech job related to software part .your task is to evaluate the resume and then you must consider the job market is very competitive and you should provie best assistance for genrating a professional cover letter based on resume.

        resume: {text}

        i want the resopnse like :
        cover letter:
        (cover letter here)

        don't do anything else just respond with cover letter only.please maintain cover letter format write name , address and other details one in line.
    """
    return prompt

st.title("Resume Analyzer")
st.text("Optimize your resume for ATS success. Upload now for instant feedback!")
jd = st.text_area("Paste the Job Description here")
uploaded_file = st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")

col1 , col2 , col3 = st.columns(3)
col4 , col5 = st.columns(2)
col6 , col7, col8 = st.columns(3)

response_placeholder = st.empty()

if "show_resume_form" not in st.session_state:
    st.session_state.show_resume_form = False

with col1:
    button = st.button("Job Matching",use_container_width=True)
    if button:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_resopnse(prompt1(text,jd))
            response_placeholder.write(response)

with col2:
    button = st.button("Keyword Optimization",use_container_width=True)
    if button:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_resopnse(prompt2(text,jd))
            response_placeholder.write(response)

with col3:
    button = st.button("Resume Summary Generator",use_container_width=True)
    if button:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_resopnse(prompt3(text))
            response_placeholder.write(response)

with col4:
    button = st.button("Resume Format & Grammar Check",use_container_width=True)
    if button:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_resopnse(prompt4(text,jd))
            response_placeholder.write(response)

with col5:
    button = st.button("Job Suggestions",use_container_width=True)
    if button:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_resopnse(prompt5(text))
            response_placeholder.write(response)

with col6:
    button = st.button("AI Generate Resume",use_container_width=True)
    if button:
        st.session_state.show_resume_form = True

with col7:
    button = st.button("Analyze Cover Letter",use_container_width=True)
    if button:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_resopnse(prompt7(text))
            response_placeholder.write(response)

with col8:
    button = st.button("Generate Cover Letter",use_container_width=True)
    if button:
        if uploaded_file is not None:
            text = input_pdf_text(uploaded_file)
            response = get_gemini_resopnse(prompt8(text))
            response_placeholder.write(response)

if st.session_state.show_resume_form:
    st.markdown(" ### Follow this format for your PDF resume:")
    col1 , col2 = st.columns(2)

    with col1:
        st.markdown("""
            
            1. **Personal Info**  
                - Full Name, Phone, Email  
                - LinkedIn/GitHub (optional)

            2. **Career Summary**  
                - A brief statement (2–3 sentences) summarizing your career goals, skills, and experience.
                    
            3. **Work Experience**  
                - Job Title, Company, Location  
                - Dates (e.g., Jan 2020 – Present)  
                - Key achievements (use bullet points) 
                    
            4. **Education**  
                - Degree, Institution, Location  
                - Graduation Date (e.g., May 2020) 
                - Relevant Coursework or Achievements (optional)
        """)
    with col2:
        st.markdown("""

        5. **Skills**  
            - Technical (e.g., Python, SQL)  
            - Soft (e.g., Communication, Leadership)  

        6. **Projects**  
            - Title, Description, Technologies Used  
            - Outcome (e.g., "Improved efficiency by 30%")  

        7. **Certifications** (optional)  
            - Name, Issuing Organization, Date Earned  

        8. **Languages** (optional)  
            - List with proficiency levels  

        9. **Hobbies/Interests** (optional)  
            - Brief list (e.g., "Open-source contributor")  

        10. **References** (optional)  
            - "Available upon request" or contact details  
    """)
        
    st.markdown("""
        
        ---

        ### Upload Your Resume
        Ensure your resume is in **PDF format** and follows the structure above.
    """)
    user_detailes = st.file_uploader("Upload Your Resume",type=["pdf"],help="Please upload the pdf")
    button = st.button("Generate Resume",use_container_width=True)
    if button:
        if user_detailes is not None:
            st.session_state.show_resume_form = False
            text = input_pdf_text(user_detailes)
            response = get_gemini_resopnse(prompt6(text))
            # response_placeholder.write(response)
            st.markdown(response)