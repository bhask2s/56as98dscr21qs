import os
print("Current working directory:", os.getcwd())

from flask import request, render_template, jsonify, send_file, current_app as app
from .utils import get_youtube_transcript_with_time, export_to_txt

@app.route('/')
def home():
    return render_template('home.html')

# ... (rest of the routes)


@app.route('/run', methods=['POST'])
def run_code():
    video_url = request.form['video_url']
    language = request.form['language']
    transcript_data = get_youtube_transcript_with_time(video_url, language)
    if "error" in transcript_data:
        return render_template('./templates/result.html', result=transcript_data['error'], download=False)
    filename = "transcript_last"
    filepath = export_to_txt(transcript_data['transcript'], filename)
    return render_template('result.html', result=transcript_data['transcript'], download=True, filename=filename)

@app.route('/download/<filename>')
def download_file(filename):
    filepath = f'{filename}.txt'
    return send_file(filepath, as_attachment=True)

@app.route('/api/transcribe', methods=['POST'])
def api_transcribe():
    data = request.json
    if not data or 'video_url' not in data:
        return jsonify({"error": "Invalid input, 'video_url' is required"}), 400
    
    video_url = data['video_url']
    language = data.get('language', 'pt')
    result = get_youtube_transcript_with_time(video_url, language)
    
    return jsonify(result)
