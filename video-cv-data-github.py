from openai import OpenAI
## Set the API key
client = OpenAI(api_key="API-KEY") #provide API key


MODEL="gpt-4o"



#####EXTRACTING AUDIO#######

from moviepy.editor import VideoFileClip

# Define the input video file and output audio file
mp4_file = r"PATH" #enter path
audio_path = "audio.mp3"

# Load the video clip
video_clip = VideoFileClip(mp4_file)

# Extract the audio from the video clip
audio_clip = video_clip.audio

# Write the audio to a separate file
audio_clip.write_audiofile(audio_path)

# Close the video and audio clips
audio_clip.close()
video_clip.close()

print("Audio extraction successful!")

# Transcribe the audio
#audio_path = r"C:\Users\gluci\Desktop\Work Power Europe\audio-test.mp3"
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=open(audio_path, "rb"),
)

#print(transcription)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
    {"role": "system", "content":"""

    HERE DEFINE THE DATA NEEDED IN SUMMARY

     """},
    {"role": "user", "content": [
        {"type": "text", "text": f"The audio transcription is: {transcription.text}"}
        ],
    }
    ],
    temperature=0,
)
print(response.choices[0].message.content)

