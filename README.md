- 코스피 정보 가져오기

```python
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
```

# bash에서 python telegram.py를 입력하면 나온다

