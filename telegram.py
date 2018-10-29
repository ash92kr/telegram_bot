import requests

token = '766852732:AAGe-xHUilCH0pDLroqQ3EZih29MCunBUtg'
method_name = 'getUpdates'
url = 'https://api.telegram.org/bot{0}/{1}'.format(token, method_name)
# print(url)
# print(requests.get(url))

user_id = '775707400'
method_name = "sendmessage"
msg = "안녕하세요"
msg_url= 'https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}'.format(token, method_name, user_id, msg)  # ? 뒷부분이 추가됨
# print(msg_url)
# print(requests.get(msg_url))

# update = requests.get(url).text   # url에 있는 내용을 보고 싶다
update = requests.get(url).json()
# print(update)
# print(type(update))   # string   # dictionary 형태

print(update["ok"])  # True
print(update["result"][0]["message"]["from"]["id"])  # [ ]로 출력되므로 인덱스로 접근할 수 있다
# dictionary는 [] 안에 "" 안에 키를 입력하고, 리스트는 []안에 인덱스를 입력



# 코스피 정보를 가져와서 텔레그램 봇으로 보내기
import requests
from bs4 import BeautifulSoup

user_id = update["result"][0]["message"]["from"]["id"]
method_name = "sendmessage"

url_cos = "https://finance.naver.com/sise/"
html_cos = requests.get(url_cos).text
soup_cos = BeautifulSoup(html_cos, 'html.parser')
select = soup_cos.select_one('#KOSPI_now')

msg = select.text
msg_url= 'https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}'.format(token, method_name, user_id, msg)
requests.get(msg_url)


# 멜론 웹사이트 - 401: 권한없음
# print(requests.get('https://www.melon.com/index.htm'), headers=headers)



