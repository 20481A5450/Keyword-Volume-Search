from flask import Flask, request, render_template
from googleapiclient.discovery import build
import requests
import random

app = Flask(__name__)

# Setting up YouTube API key
API_KEY = 'AIzaSyC36BG14zOq3IKtceQGWzr9r1SBWv4ujOE'

# Creating a YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_search_results(keyword, max_results=10):
    try:
        search_response = youtube.search().list(
            q=keyword,
            type='video',
            part='id',
            maxResults=max_results
        ).execute()
        video_ids = [item['id']['videoId'] for item in search_response['items']]
        total_results = search_response.get('pageInfo', {}).get('totalResults', 0)
        return video_ids, total_results
    except requests.exceptions.HTTPError as e:
        print(e)
        return [], 0

def get_video_details(video_id):
    try:
        video_response = youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        ).execute()

        return video_response['items'][0]
    except requests.exceptions.HTTPError as e:
        print(e)
        return {}
def estimate_search_volume(video_data):
    try:
        views = int(video_data['statistics'].get('viewCount', 0))
        likes = int(video_data['statistics'].get('likeCount', 0))
        comments = int(video_data['statistics'].get('commentCount', 0))
        
        # Relative weights for engagement metrics
        view_weight = 0.6
        like_weight = 0.3
        comment_weight = 0.1
        
        # Calculating estimated search volume based on engagement metrics
        search_volume = views * view_weight + likes * like_weight + comments * comment_weight
        
        return int(search_volume)
    except requests.exceptions.HTTPError as e:
        print(e)
        return 0

@app.route('/', methods=['GET', 'POST'])
def index():
    search_results = []
    video_details = {}
    search_volume = 0
    graph_data = []

    if request.method == 'POST':
        keyword = request.form.get('keyword')
        if keyword:
            search_results, total_results = get_search_results(keyword)
            search_volume = total_results
            
            if search_results:
                video_id = search_results[0]
                video_details = get_video_details(video_id)
                search_volume = estimate_search_volume(video_details)
                
                # Generate placeholder search volume data for the past 12 months
                graph_data = [random.randint(1000, 10000) for _ in range(12)]

    return render_template('index.html', search_results=search_results, search_volume=search_volume,
                           graph_data=graph_data, video_details=video_details)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
