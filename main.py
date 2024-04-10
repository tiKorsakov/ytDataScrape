import os
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scopes for accessing YouTube Data API
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        '', SCOPES
    )
    credentials = flow.run_local_server()
    return build('youtube', 'v3', credentials=credentials)

def get_watch_history(youtube, start_date, end_date):
    request = youtube.videos().list(
        part='snippet',
        myRating='like',
        maxResults=50,
        publishedAfter=start_date + 'T00:00:00Z',
        publishedBefore=end_date + 'T23:59:59Z'
    )
    response = request.execute()
    return response

if __name__ == '__main__':
    youtube = get_authenticated_service()

    start_date = '2023-09-20'
    end_date = '2023-09-24'

    watch_history = get_watch_history(youtube, start_date, end_date)
    print(watch_history)
