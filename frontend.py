import streamlit as st
from backend import comp_process


def frontend():

    st.set_page_config(page_title='Youtube-GPT', layout='wide' )
    st.title('Chat with :red[Youtube] Video!')


    question = st.text_input('Ask the question below')

    with st.sidebar:
        with st.form(key='my_form'):
            api_key = st.text_input("Enter the OpenAI API key below:", placeholder='openai api key', type='password')
            url = st.text_input("Enter Youtube url below:", placeholder='paste url here:')
            submit_button = st.form_submit_button(label='Submit')


    if url and api_key is not None:
        if question:
            ans  = comp_process(apikey=api_key, url=url, question=question)
            st.write(ans)   
    

if __name__ == "__main__":
    frontend()
