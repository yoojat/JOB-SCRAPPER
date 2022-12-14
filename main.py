# from extractors.wwr import extract_wwr_jobs

# jobs = extract_wwr_jobs("python")
# print(jobs)

from requests import get
# import selenium # 셀레니움 설치
from selenium import webdriver  # 파이썬에서 브라우저를 시작할수 있게 함
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()  # 리플잇 안에서 브라우저가 동작하게 몇가지 옵션을 전달해야함
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

# print(browser.page_source)

results = []

soup = BeautifulSoup(browser.page_source, 'html.parser')

job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False)
print(len(jobs))
for job in jobs:
  zone = job.find("div", class_="mosaic-zone")
  # job이 아닌 li를 찾기위한 과정
  if zone == None:
    h2 = job.find("h2", class_="jobTitle")
    # anchor = job.select("h2 a")
    anchor = job.select_one("h2 a")
    title = anchor['aria-label']
    link = anchor['href']
    # print(anchor)

    company = job.find("span", class_="companyName")
    location = job.find("div", class_="companyLocation")
    # print(title, link)
    job_data={
      "link":f"https://kr.indeed.com{link}",
      "company":company.string,
      "location":location.string,
      "position":title
    }
    print("////\n////")
    results.append(job_data)
for result in results:
  print(result,"\n//////\n")