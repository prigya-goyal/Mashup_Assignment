# Mashup_Assignment

# MASHUP GENERATOR

This project generates an **Audio Mashup** from YouTube videos in two forms:
1. Command Line Tool
2. Web Application using Streamlit

The mashup generator searches YouTube videos of a given singer, downloads audio, trims each clip to a fixed duration, and merges them into one final mashup file.

---

## Part-1: Command Line Tool

The mashup can be generated directly from the terminal using a Python script.

## Input Parameters
The program requires three inputs:

- Singer Name  
- Number of Videos  
- Duration (in seconds)  

---

## Command Line Usage

```bash
python 102313061.py <singer_name> <number_of_videos> <duration_in_seconds>

```

## Example
python 102313061.py arijit singh 5 30

---

## Output

The program generates:
-Downloaded audio clips
-Final merged mashup file
-The final mashup file is saved in the same directory.

---

## Part-2: Web Application (Streamlit)

A web interface is created using Streamlit where users can:
-Enter singer name
-Enter number of videos
-Enter duration
-Generate mashup
-Download final mashup file

---

## How to Run Web App
streamlit run 102313061.py

---

## Then open in browser:
http://localhost:8501

---

## Project Structure

-Part_1/
    102313061.py
    requirements.txt

-Part_2/
    102313061.py
    app.py

-README.md
-requirements.txt

---

## Notes

-Internet connection is required.
-FFmpeg must be installed and added to system PATH.
-Number of videos and duration must be valid positive integers.

---

## Requirements

-Python 3.x
-streamlit
-pydub
-yt-dlp
-moviepy

---

## Author
Prigya Goyal

---

## License
This project is released under the MIT License for educational purposes. See the LICENSE file for details.
