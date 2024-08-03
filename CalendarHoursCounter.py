from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta, timezone

# ID календаря "Учеба"
CALENDAR_ID = '3ea85527e406a2b94229ed0f2b70397fbe60f7fa4b1789e3a9c0fdb7546c1e3f@group.calendar.google.com'

# Путь к файлу с ключом от сервисного аккаунта в Google Cloud
CREDENTIALS_FILE = './calendarintegration-431411-8dba073a9c3c.json'

def main():
    credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=['https://www.googleapis.com/auth/calendar.readonly'])
    service = build('calendar', 'v3', credentials=credentials)

    # Получить начало и конец текущей недели
    now = datetime.now(timezone.utc)
    start_of_week = now - timedelta(days=now.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    # Получить события из календаря
    events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=start_of_week.isoformat(), timeMax=end_of_week.isoformat(), singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    total_duration = 0
    for event in events:
        start = datetime.fromisoformat(event['start'].get('dateTime', event['start'].get('date')))
        end = datetime.fromisoformat(event['end'].get('dateTime', event['end'].get('date')))
        duration = end - start
        total_duration += duration.total_seconds()

    total_hours = total_duration / 3600
    print(f'Общее время событий на этой неделе: {total_hours:.2f} часов')

if __name__ == '__main__':
    main()
