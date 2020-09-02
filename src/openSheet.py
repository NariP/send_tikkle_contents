import gspread
from oauth2client.service_account import ServiceAccountCredentials
from src.Data.sensitiveData import spreadsheet_url, json_file_name, right_pwd

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

# 스프레드시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기
worksheet = doc.worksheet('설문지 응답 시트1')

# 비밀번호 리스트(B열) 가져오기
pwd_list = worksheet.col_values(3)[1:]
final_idx = len(pwd_list) + 1
print(pwd_list)

i = 0
right_idx_list = []
for pwd in pwd_list:
    if pwd == right_pwd:
        right_idx_list.append(i)
        print(right_idx_list)
        i += 1
    else:
        print("비밀번호가 일치하지 않음")

# 이메일 리스트(B열) 가져오기
email_list = worksheet.col_values(2)[1:]
print(email_list)

real_email_list = []
for idx in right_idx_list:
    real_email_list.append(email_list[idx])

print(real_email_list)