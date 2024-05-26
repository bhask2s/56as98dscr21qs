from youtube_transcript_api import YouTubeTranscriptApi

# Function to export text to a .txt file
def export_to_txt(text, filename):
    filepath = f'{filename}.txt'
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)
    return filepath

# Function to get YouTube transcript with time
def get_youtube_transcript_with_time(video_url, language='pt'):
    video_id = video_url.split('watch?v=')[1]

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
    except:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
        except Exception as e:
            return {"error": str(e)}

    transcript_with_time = ""
    for item in transcript:
        start_time = item['start']
        minutes = int(start_time // 60)
        seconds = int(start_time % 60)
        formatted_time = f'{minutes:02d}:{seconds:02d}'
        text = item['text']
        transcript_with_time += f"Time: {formatted_time}s: {text}\n"

    return {"transcript": transcript_with_time}
