import streamlit as st
import zipfile
import smtplib
from email.message import EmailMessage
from mashup import create_mashup


SENDER_EMAIL = "goyalprigya@gmail.com"
APP_PASSWORD = "zfjfgpdqwcgreknl"   

st.set_page_config(page_title="Mashup Generator", page_icon="🎵")

st.title("🎵 Mashup Generator")

singer = st.text_input("Singer Name")
videos = st.number_input("Number of Videos (>10)", min_value=11)
duration = st.number_input("Duration (>20 sec)", min_value=21)
receiver_email = st.text_input("Receiver Email")

if st.button("Generate Mashup"):

    if not singer or not receiver_email:
        st.error("Please fill all fields.")
    else:
        with st.spinner("Creating mashup... please wait ⏳"):
            create_mashup(singer, videos, duration, "output.mp3")

        st.success("Mashup created successfully! ✅")

        zip_filename = "mashup.zip"
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            zipf.write("output.mp3")

        try:
            msg = EmailMessage()
            msg["Subject"] = "Your Mashup File 🎵"
            msg["From"] = SENDER_EMAIL
            msg["To"] = receiver_email
            msg.set_content("Please find your mashup ZIP attached.")

            with open(zip_filename, "rb") as f:
                file_data = f.read()

            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="zip",
                filename=zip_filename
            )

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(SENDER_EMAIL, APP_PASSWORD)
                smtp.send_message(msg)

            st.success("ZIP file sent to email successfully 📧")

        except Exception as e:
            st.error(f"Email failed: {e}")

        with open("output.mp3", "rb") as f:
            st.download_button(
                label="Download Mashup",
                data=f,
                file_name="output.mp3"
            )

