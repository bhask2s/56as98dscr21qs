from flask import Blueprint, render_template, request, jsonify, send_file
from .utils import get_youtube_transcript_with_time, export_to_txt

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/run', methods=['POST'])
def run_transcript():
    video_url = request.form['video_url']
    language = request.form['language']
    
    transcript_result = get_youtube_transcript_with_time(video_url, language)
    
    if 'error' in transcript_result:
        transcription = transcript_result['error']
        return render_template('result.html', transcription=transcription)
    else:
        transcription = transcript_result['transcript']
        filepath = export_to_txt(transcription, 'transcript')
        return send_file(filepath, as_attachment=True, download_name='transcript.txt')

@main.route('/api/transcript', methods=['POST'])
def api_transcript():
    data = request.get_json()
    video_url = data.get('video_url')
    language = data.get('language', 'pt')
    
    transcript_result = get_youtube_transcript_with_time(video_url, language)
    
    if 'error' in transcript_result:
        return jsonify({"error": transcript_result['error']}), 400
    
    return jsonify({"transcript": transcript_result['transcript']})
