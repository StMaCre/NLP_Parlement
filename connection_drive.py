from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload
import os
import pickle
import io


SCOPES = ['https://www.googleapis.com/auth/drive']
folder_id = 'YOUR_FOLDER_ID'


def download_file(service, file_id, filename, download_path):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()

    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    fh.seek(0)

    with open(os.path.join(download_path, filename), 'wb') as f:
        f.write(fh.read())
        f.close()


def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r'YOUR_JSON_FILES', SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    results = service.files().list(
        q="'" + folder_id + "' in parents",
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
            filename = item['name']
            download_file(service, item['id'], filename, 'pdf')

    # Now all the files have been downloaded, you can read them one by one
    for item in items:
        filename = item['name']
        with open(filename, 'r') as f:
            content = f.read()
        print(content)


if __name__ == '__main__':
    main()
