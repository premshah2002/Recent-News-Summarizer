import streamlit as st
from exa_py import Exa
from together import Together
from datetime import datetime, timedelta

st.set_page_config(layout="wide")

st.subheader("Hi, I am Exe. I can fetch and summarize latest news on topic of your choice 📰😎")

SYSTEM_MESSAGE = "You are a helpful assistant that generates search queries based on user questions. Only generate one search query."
USER_QUESTION = st.text_input("Enter topic")

# Initialize session state
if 'summarize' not in st.session_state:
    st.session_state.summarize = [False] * 5
if 'summaries' not in st.session_state:
    st.session_state.summaries = [""] * 5

if USER_QUESTION:
    exa = Exa(st.secrets['EXA_API_KEY'])
    client = Together(api_key=st.secrets['TOGETHER_API_KEY'])
    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": USER_QUESTION},
        ],
    )

    search_query = response.choices[0].message.content

    one_week_ago = (datetime.now() - timedelta(days=7))
    date_cutoff = one_week_ago.strftime("%Y-%m-%d")

    search_response = exa.search_and_contents(
        search_query, use_autoprompt=True, start_published_date=date_cutoff, num_results=5
    )
    
    results = search_response.results
    st.write("Top 5 news articles rn: 👇")
    for i, result in enumerate(results):
        st.markdown(f"""
        <div style="border: 1px solid #888888; padding: 10px; margin-bottom: 10px;">
            <p>{result.text}</p>
            <p>Source: {result.id}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Check if the button is clicked
        if st.button(f"Summarize Article {i+1}"):
            st.session_state.summarize[i] = True
        
        # If the button was clicked, generate the summary
        if st.session_state.summarize[i]:
            if not st.session_state.summaries[i]:
                SYSTEM_MESSAGE_2 = "You are a helpful assistant that briefly summarizes the content of a webpage. Summarize the users input."
                response = client.chat.completions.create(
                    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
                    messages=[
                        {"role": "system", "content": SYSTEM_MESSAGE_2},
                        {"role": "user", "content": result.text},
                    ],
                )
                st.session_state.summaries[i] = response.choices[0].message.content
            
            st.write(st.session_state.summaries[i])
