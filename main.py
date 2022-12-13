import openai
import os
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

# Page Config
st.set_page_config(page_title="CV Shop AI Assistant | Cover Letter Writer")


# Title
st.title("CV Shop AI Assistant")

# Header
st.header("Cover Letter Writer")

# Text Inputs

# Full Name
full_name = st.text_input("Your Full Name")
# Field of Expertise
field_of_expertise = st.text_input(
    "Your Field Name", help="Tell us your field of expertise (e.g. Software Engineer, UI/UX Designer, Content Writer etc.)")
# check box
if st.checkbox("Would you like to tell us more about yourself?"):
    # more personal info
    more_personal_info = st.text_area(
        "Tell us more about yourself (Optional)", help="Tell us more about yourself (e.g. your hobbies, your interests, your skills etc.)")
else:
    more_personal_info = ""
# Company Name
company_name = st.text_input(
    "Company Name", help="The name of the company you are applying to.")
# check box
if st.checkbox("Would you like to tell us more about the company?"):
    # more company info
    more_company_info = st.text_area("Tell us more about the company (Optional)",
                                     help="Tell us more about the company (e.g. the company's mission, the company's values etc.)")
else:
    more_company_info = ""
# Job Title
job_title = st.text_input(
    "Job Title", help="The job title you are applying for.")
# check box
if st.checkbox("Would you like to tell us more about the job?"):
    # more job info
    more_job_info = st.text_area("Tell us more about the job (Optional)",
                                 help="Tell us more about the job (e.g. the job description, the job requirements etc.)")
else:
    more_job_info = ""
# check if all fields are filled
while full_name == "" or field_of_expertise == "" or company_name == "" or job_title == "":
    st.warning("Please fill in all the fields to Generate.")
    break
else:
    # Submit button
    if st.button("Generate Cover Letter"):
        # request input
        request_input = f"""
                {full_name}: My name is {full_name}. I am a {field_of_expertise}. {more_personal_info} I want to apply for the {job_title} position at {company_name}. {more_company_info} {more_job_info}
                AI, Please Genarate a cover letter for this job.
                \nAI:
                """

        # show loading
        with st.spinner("Generating..."):
            # setting api key
            #openai.api_key = os.getenv("OPENAI_API_KEY")
            response = {
                "choices": [
                    {
                        "text": "There was a problem with the request. Please try again after sometime."
                    }
                ],
            }
            # getting response
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=request_input,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                stop=["\nAI:"],
                frequency_penalty=0,
                presence_penalty=0
            )
            # subheading
            st.subheader("Your Cover Letter")
            # echo response
            reply = response.choices[0].text
            # change reply to string
            reply = str(reply)
            st.write(reply)
            

