from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# If modifying these scopes, delete the file token.json.

class sheets:
    
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

        # The ID and range of a sample spreadsheet.
        sheetID=str(open('./SAMPLE_SPREADSHEET_ID.txt','r').read())
        self.SAMPLE_SPREADSHEET_ID = sheetID
        self.SAMPLE_RANGE_NAME = 'Sheet1!A8:B15'
        self.value=[]


    def authenticate(self):
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                self.flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.creds = self.flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as self.token:
                self.token.write(self.creds.to_json())

        self.service=build('sheets', 'v4', credentials=self.creds)

    # Call the Sheets API
    def getSheetValue(self):
        self.sheet = self.service.spreadsheets()
        self.result =self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                    range=self.SAMPLE_RANGE_NAME).execute()
        self.value= self.result.get('values', [])
        return self.value

        