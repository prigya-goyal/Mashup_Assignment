# Mashup Assignment - Part 1

## Student Details
**Roll Number:** 102313061

---

## Project Description

This project generates an audio mashup from YouTube videos.

The script:
- Searches for songs on YouTube
- Downloads audio files
- Trims each audio to a fixed duration
- Merges multiple audio clips into one final mashup file

---

## Folder Structure

Mashup_Assignment/
└── Part_1/
    ├── 102313061.py
    ├── requirements.txt
    └── README.md

---

## Installation

### Step 1: Clone the Repository

``bash
git clone <your-repo-link>
Step 2: Navigate to Part_1 Folder
cd Part_1
Step 3: Install Dependencies
pip install -r requirements.txt
How to Run
python 102313061.py <singer_name> <number_of_videos> <duration_in_seconds>
Example
python 102313061.py arijit singh 5 30
This command will:

Download 5 songs

Trim each to 30 seconds

Merge them into one mashup file

##Output
The final mashup audio file will be saved in the same directory.

##Requirements
Python 3.x

FFmpeg installed and added to system PATH

Internet connection

##Libraries Used
requests

pydub

moviepy

yt-dlp
