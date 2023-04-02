import json
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # load the environment variables from .env file
API_KEY = os.getenv('API_KEY')

playlist_id = 'PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo'
url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&key={API_KEY}'
videos = {}

next_page_token = None
while True:
    if next_page_token:
        next_url = url + f'&pageToken={next_page_token}'
    else:
        next_url = url

    response = requests.get(next_url).json()

    for item in response['items']:
        video_id = item['snippet']['resourceId']['videoId']
        title = item['snippet']['title']

        video_url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet&id={video_id}&key={API_KEY}'
        video_response = requests.get(video_url).json()

        try:
            statistics = video_response['items'][0]['statistics']
            view_count = statistics['viewCount']
            upload_date = item['snippet']['publishedAt']
            video = {'video_id': video_id, 'title': title, 'view_count': view_count, 'upload_date': upload_date}
            videos[len(videos)+1] = video
        except IndexError:
            print(f"No statistics found for video ID {video_id}")
        continue
  
    try:
        next_page_token = response['nextPageToken']
    except KeyError:
        break

formatted_videos = {}

for i, video in videos.items():
    formatted_videos[i] = {'video_id': video['video_id'], 'title': video['title'], 'view_count': video['view_count']}

json_data = json.dumps(formatted_videos)

with open('data.json', 'w') as f:
    f.write(json_data)

#309 total video data because 3 of them have been privated or removed from YouTube.