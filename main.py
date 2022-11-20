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
  jobs = soup.find_all('section', class_='jobs')
  # print(len(jobs))  # 길이 출력
  for job_section in jobs:
    job_posts = (job_section.find_all('li'))  # jobs section안에 있는 li를 다가지고 옴
    job_posts.pop(-1) # 마지막 항목 제거

    for post in job_posts:
      print(post)
      print("//////")
  # job class를 가진 section을 찾는 것, class_라고 적는 것 주의(class라는 키워드를 이미 파이썬에서 사용중이기 때문)
