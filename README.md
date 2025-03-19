# YouTube Transcript to Detailed Notes Converter 🎥✍️  

This Streamlit-based web app extracts and summarizes YouTube video transcripts using **Google Gemini AI**. Simply enter a YouTube video link, and the app will:  

✅ Extract the transcript from the video  
✅ Summarize key points in a structured format  
✅ Generate relevant hashtags for better categorization  

## 🔧 Features  
- Automatic transcript extraction using `youtube_transcript_api`  
- AI-powered summarization with **Google Gemini**  
- Error handling for invalid links & API failures  
- Displays video thumbnail for better reference  

## 🛠️ Tech Stack  
- **Python** (Streamlit, Google Generative AI, `dotenv`)  
- **YouTube Transcript API** for fetching subtitles  
- **Google Gemini AI** for text summarization  

## 🚀 How to Use  
1. Clone the repo:  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2.Install dependencies:
bash
pip install -r requirements.txt
3.Set up your .env file with:
GOOGLE_API_KEY=your_api_key
4.Run the app:
bash
streamlit run app.py or app2.py
