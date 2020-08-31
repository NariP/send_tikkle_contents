import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

json_file_name = '../tikkle-288117-d97e31432e3f.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1dKMGwAPf22iqM3-JrN7H2Bwh2lDr6_UKF1jD0vxyILQ/edit#gid=475218338'

# 스프레드시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기
worksheet = doc.worksheet('설문지 응답 시트1')

# 열 데이터 가져오기
column_data = worksheet.col_values(2)
print(column_data)