from flask import Flask, request, render_template
import requests
import random
from googleapiclient.discovery import build

app = Flask(__name__)

# Set your YouTube API key
API_KEY = 'AIzaSyC36BG14zOq3IKtceQGWzr9r1SBWv4ujOE'

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_search_results(keyword, max_results=10):
    search_response = youtube.search().list(
        q=keyword,
        type='video',
        part='id',
        maxResults=max_results
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response['items']]
    total_results = search_response.get('pageInfo', {}).get('totalResults', 0)
    
    return video_ids, total_results

def get_video_details(video_id):
    video_response = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()

    return video_response['items'][0]

def get_related_videos(video_id, max_results=5):
    search_response = youtube.search().list(
        relatedToVideoId=video_id,
        type='video',
        part='id,snippet',
        maxResults=max_results,
        key=API_KEY
    ).execute()

    related_videos = []
    for item in search_response['items']:
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        related_videos.append({'id': video_id, 'title': video_title})

    return related_videos

@app.route('/', methods=['GET', 'POST'])
def index():
    search_results = []
    video_details = {}
    related_videos = []
    search_volume = 0
    graph_data = []

    if request.method == 'POST':
        keyword = request.form.get('keyword')
        if keyword:
            search_results, search_volume = get_search_results(keyword)
            
            if search_results:
                video_id = search_results[0]
                video_details = get_video_details(video_id)
                related_videos = get_related_videos(video_id)
                
                # Generate random search counts for the past 12 months (placeholder data)
                graph_data = [random.randint(1000, 10000) for _ in range(12)]

    return render_template('index.html', search_results=search_results, search_volume=search_volume,
                       graph_data=graph_data, video_details=video_details, related_videos=related_videos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

