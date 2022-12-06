# from extractors.wwr import extract_wwr_jobs

# jobs = extract_wwr_jobs("python")
# print(jobs)

from requests import get
from bs4 import BeautifulSoup

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")

print(response) # 403 error 접근 금지 봇으로 부터 보호, 차단됨
 
if response.status_code != 200:
  print("Cant request page")
else:
  print(response.text)

# soup = BeautifulSoup(response.text, "html.parser")
# job_list = soup.find("ul", class_="jobsearch-ResultList")
# jobs = job_list.find_all("li", recursive= False)
# for job in jobs:
#   print(job)
#   print("////////")