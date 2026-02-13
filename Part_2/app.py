import streamlit as st
import importlib.util
import os

# Dynamically import 102313061.py
spec = importlib.util.spec_from_file_location("mymodule", "102313061.py")
mymodule = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mymodule)

create_mashup = mymodule.create_mashup

st.set_page_config(page_title="Mashup Generator", page_icon="🎵")

st.title("🎵 Mashup Generator (Web Version)")

singer = st.text_input("Singer Name")
videos = st.number_input("Number of Videos (>10)", min_value=11)
duration = st.number_input("Duration (>20 sec)", min_value=21)
receiver_email = st.text_input("Receiver Email")

if st.button("Generate Mashup"):

    if not singer or not receiver_email:
        st.error("Please fill all fields.")
    else:
        with st.spinner("Creating mashup... please wait ⏳"):
            create_mashup(
                singer,
                videos,
                duration,
                "output.mp3",
                receiver_email
            )

        st.success("Mashup created and email sent successfully! ✅")

        # Download button
        if os.path.exists("output.mp3"):
            with open("output.mp3", "rb") as f:
                st.download_button(
                    label="Download Mashup",
                    data=f,
                    file_name="output.mp3"
                )
