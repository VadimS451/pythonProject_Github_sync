from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime, timedelta, timezone

# ID календаря "Учеба"
CALENDAR_ID = '3ea85527e406a2b94229ed0f2b70397fbe60f7fa4b1789e3a9c0fdb7546c1e3f@group.calendar.google.com'

# Путь к файлу с ключом от сервисного аккаунта в Google Cloud
CREDENTIALS_FILE = './calendarintegration-431411-9b6b001b20aa.json'


def main():
    credentials = (service_account.Credentials.from_service_account_file
                   (CREDENTIALS_FILE, scopes=['https://www.googleapis.com/auth/calendar.readonly']))
    service = build('calendar', 'v3', credentials=credentials)

    # Получить начало и конец текущей недели с нуля часов
    now = datetime.now(timezone.utc)
    start_of_week = datetime(now.year, now.month, now.day, tzinfo=timezone.utc) - timedelta(days=now.weekday())
    end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)

    # Получить события из календаря
    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start_of_week.isoformat(),
        timeMax=end_of_week.isoformat(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    # Запрос ключевого слова
    keyword = input("Введите ключевое слово встречающееся в событиях календаря: ")

    total_duration = 0
    for event in events:
        # Проверка наличия ключевого слова (если введено)
        if keyword and keyword.lower() not in event['summary'].lower():
            continue  # Пропустить событие, если ключевое слово не найдено

        # # Проверка наличия слова "учеба" в названии события
        # if 'учеба' not in event['summary'].lower():
        #     continue  # Пропустить событие, если "учеба" не найдено

        start = datetime.fromisoformat(event['start'].get('dateTime', event['start'].get('date')))
        end = datetime.fromisoformat(event['end'].get('dateTime', event['end'].get('date')))
        duration = end - start
        total_duration += duration.total_seconds()

    total_hours = total_duration / 3600
    print('Вывод переменной "now"', now)
    print('Начало недели:', start_of_week)
    print('Конец недели:', end_of_week)
    print(f'Общее время событий на этой неделе: {total_hours:.2f} часов')


if __name__ == '__main__':
    main()
