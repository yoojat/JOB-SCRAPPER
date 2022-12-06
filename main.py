# from extractors.wwr import extract_wwr_jobs

# jobs = extract_wwr_jobs("python")
# print(jobs)

from requests import get
# import selenium # 셀레니움 설치
from selenium import webdriver # 파이썬에서 브라우저를 시작할수 있게 함
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()# 리플잇 안에서 브라우저가 동작하게 몇가지 옵션을 전달해야함
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

print(browser.page_source)



# soup = BeautifulSoup(response.text, "html.parser")
# job_list = soup.find("ul", class_="jobsearch-ResultList")
# jobs = job_list.find_all("li", recursive= False)
# for job in jobs:
#   print(job)
#   print("////////")