import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt for summarization
prompt = """You are a YouTube video summarizer. You will take the transcript text, summarize the entire video in points, and provide important hashtags related to the video."""

def extract_transcript_details(youtube_video_url):
    try:
        # Extract video ID from the URL
        parsed_url = urlparse(youtube_video_url)
        video_id = parse_qs(parsed_url.query).get("v", [None])[0]

        if not video_id:
            raise ValueError("Invalid YouTube URL")

        # Fetch transcript using YouTubeTranscriptApi
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join(i["text"] for i in transcript_text)

        return transcript
    except Exception as e:
        return f"Error: {str(e)}"

def generate_gemini_content(transcript_text, prompt):
    try:
        # Use the Gemini Pro model
        model = genai.GenerativeModel("gemini-pro")

        # Generate content using the model
        response = model.generate_content(prompt + transcript_text)

        # Return the generated text
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app
st.title("YouTube Transcript to Detailed Notes Converter")

# Input for YouTube video link
youtube_link = st.text_input("Enter YouTube video link:")

if youtube_link:
    # Extract video ID and display thumbnail
    parsed_url = urlparse(youtube_link)
    video_id = parse_qs(parsed_url.query).get("v", [None])[0]

    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True) #Corrected thumbnail url
    else:
        st.error("Invalid YouTube URL. Please enter a valid link.")

# Button to generate detailed notes
if st.button("Get Detailed Notes"):
    # Extract transcript
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text and not transcript_text.startswith("Error"):
        # Generate summary using Gemini
        summary = generate_gemini_content(transcript_text, prompt)

        if summary.startswith("Error"):
            st.error(summary)
        else:
            st.markdown("## Detailed Notes:")
            st.write(summary)
    else:
        st.error(transcript_text)