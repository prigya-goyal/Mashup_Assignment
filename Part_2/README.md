# Mashup Assignment - Part 2 (Streamlit Web App)

## Student Details
**Roll Number:** 102313061

---

## Project Overview

This project is a Streamlit-based web application that generates an audio mashup from YouTube videos.

Users can:
- Enter singer name
- Enter number of videos
- Enter duration (in seconds)
- Generate mashup using a simple web interface

The system:
- Searches YouTube videos
- Downloads audio
- Trims audio to specified duration
- Merges multiple clips into one mashup file
- Provides the final mashup for download

---

## Folder Structure

Mashup_Assignment/
└── Part_2/
    ├── 102313061.py
    ├── requirements.txt
    └── README.md

---

## Installation

### Step 1: Clone Repository

```bash
git clone <your-repo-link>
Step 2: Navigate to Part_2 Folder
cd Part_2
Step 3: Install Required Packages
pip install -r requirements.txt
How to Run
Since this is a Streamlit application, run:

streamlit run 102313061.py
After running the command, open the browser and go to:

http://localhost:8501
Requirements
Python 3.x

FFmpeg installed and added to system PATH

Internet connection

Libraries Used
streamlit

pydub

yt-dlp

requests (if used)

moviepy (if used)

Output
The generated mashup file is created and made available for download through the web interface.

