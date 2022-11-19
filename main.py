from requests import get
from bs4 import BeautifulSoup


base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"
# 다양한 검색을 위해 변수 선언

response = get(f"{base_url}{search_term}")
# f를 사용하면 문자열 안에 변수를 넣을 수 있음

if response.status_code != 200:
  print("Can't request website.")
else:
  soup = BeautifulSoup(response.text, 'html.parser')
  print(soup.find_all('title')) # title 태그를 찾아줌