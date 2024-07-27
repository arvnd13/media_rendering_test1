import streamlit as st
import random
import time

# .streamlit/secrets.toml
#password = "streamlit123"


#st.text_input('user ID')

#st.radio('Are you Interested in Child care Videos ?', ['Yes','No'])

#st.title("Upload Child care Photos")


#from streamlit.elements.image import image_to_url, MAXIMUM_CONTENT_WIDTH
#from PIL import Image
#
#img = st.file_uploader("upload image", type=["jpg", "png"])
#if img:
#    test = Image.open(img)
#    width, height = test.size  # width is needed for image_to_url()
#    if width > MAXIMUM_CONTENT_WIDTH:
#        width = MAXIMUM_CONTENT_WIDTH  # width is capped at 2*730 https://github.com/streamlit/streamlit/blob/949d97f37bde0948b57a0f4cab7644b61166f98d/lib/streamlit/elements/image.py#L39
#    st.image(img)
#    st.write(
#        image_to_url(
#            image=img,
#            width=width,
#            clamp=False,
#            channels="RGB",
#            output_format=img.type,
#            image_id=img.id,  # each uploaded file has a file.id
#        )
#    )
#
#    
#
#st.subheader("audio1:")
#st.audio("audio.mp3")
st.subheader("Online video URL: ")
st.video("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4", format="video/mp4")





st.title("Veera Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is your name"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": "Welcome !!"})
    with st.chat_message("assistant"):
        st.markdown("welcome !!.")
  
