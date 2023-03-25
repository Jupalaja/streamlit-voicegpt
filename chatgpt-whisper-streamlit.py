# Import required libraries
import config
import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = config.OPENAI_API_KEY

# Set up Streamlit interface
st.subheader("AI Assistant : Streamlit + OpenAI: `stream` *argument*")

# Get user input
user_input = st.text_input(
    "You: ", placeholder="Ask me anything ...", key="input")

# Set up submit button
if st.button("Submit", type="primary"):
    st.markdown("----")
    res_box = st.empty()
    report = []
    # Send user input to OpenAI model
    for resp in openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': user_input}
        ],
        temperature=0,
        stream=True
    ):
        # join method to concatenate the elements of the list
        # into a single string,
        # then strip out any empty strings
        report.append(resp.choices[0]['delta'].get('content', ''))
        result = "".join(report).strip()
        result = result.replace("\n", "")
        res_box.markdown(f'*{result}*')

# Display a separator line
st.markdown("----")
