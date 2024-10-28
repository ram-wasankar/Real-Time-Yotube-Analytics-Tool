from flask import Flask, render_template, request
from youtube_data import get_youtube, get_channel_stats, get_playlist_id, get_video_ids, get_video_details

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/youtube/form')
def youtube_form():
    return render_template('forms/youtube_form.html')

@app.route('/youtube/process', methods=['POST'])
def process_youtube_form():
    channel_id = request.form['channel_id']
    
    # Fetch YouTube data
    youtube = get_youtube()
    channel_stats = get_channel_stats(youtube, channel_id)
    
    if not channel_stats:
        return render_template('error.html', message="Error fetching channel data")
    
    playlist_id = get_playlist_id(youtube, channel_id)
    video_ids = get_video_ids(youtube, playlist_id)
    video_details = get_video_details(youtube, video_ids)
    
    for video in video_details:
        video['Views'] = int(video['Views'])
        video['Likes'] = int(video['Likes'])
    
    return render_template('youtube_dashboard.html', channel_stats=channel_stats, video_details=video_details)

@app.route('/youtube/dashboard')
def youtube_dashboard():
    return "YouTube Dashboard"

if __name__ == '__main__':
    app.run(debug=True)
