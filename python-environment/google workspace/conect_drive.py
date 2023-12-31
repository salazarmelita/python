from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = "salazarmelita-py.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = "1KsznK8ibZTCV1GkYzW1VbnLOYscfT7aP"
file_names = ["python-summary.pdf"]
mime_types = ['application/pdf']

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        "name" : file_name,
        "parents" : [folder_id]
    }

    media = MediaFileUpload("./media/{0}".format(file_name), mimetype=mime_type)

    service.files().create(
        body=file_metadata,
        media_body = media,
        fields = "id"
    ).execute()