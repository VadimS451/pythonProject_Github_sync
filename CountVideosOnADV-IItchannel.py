from googleapiclient.discovery import build
from datetime import datetime

# Вставляем API ключ из файла
api_key = 'YOUR_API_KEY'
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']


channel_id = 'UC-sAMvDe7gTmBbub-rWljZg'  # Правильный ID канала ADV-IT

# Создаем объект YouTube API
youtube = build('youtube', 'v3', developerKey=api_key)

def get_videos_in_date_range(channel_id, start_date, end_date):
    videos = []
    next_page_token = None
    start_date_limit = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%SZ')
    end_date_limit = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%SZ')

    while True:
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            maxResults=50,
            order='date',
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            video_date = datetime.strptime(item['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            print(f"Video Title: {item['snippet']['title']}, Published At: {video_date}")
            if start_date_limit <= video_date < end_date_limit:
                videos.append(item)

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return videos

# Укажи начальную и конечную даты в формате 'YYYY-MM-DDTHH:MM:SSZ'
start_date = '1992-01-01T00:00:00Z'
end_date = '2019-05-24T00:00:00Z'
videos = get_videos_in_date_range(channel_id, start_date, end_date)

print(f"Количество видео с {start_date} до {end_date}: {len(videos)}")
