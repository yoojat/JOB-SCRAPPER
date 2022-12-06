from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
  # 다양한 검색을 위해 변수 선언

  response = get(f"{base_url}{keyword}")
  # f를 사용하면 문자열 안에 변수를 넣을 수 있음

  if response.status_code != 200:
    print("Can't request website.")
  else:
    results = []
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('section', class_='jobs')
    # job class를 가진 section을 찾는 것, class_라고 적는 것 주의(class라는 키워드를 이미 파이썬에서 사용중이기 때문)
    # print(len(jobs))  # 길이 출력
    for job_section in jobs:
      job_posts = (job_section.find_all('li'))  # jobs section안에 있는 li를 다가지고 옴
      job_posts.pop(-1)  # 마지막 항목 제거

      for post in job_posts:
        # print(post) # 여기서 post는 하나의 beautifulsoup 엔티티이기도 함
        anchors = post.find_all('a')
        anchor = anchors[1]  # 첫번째 것은 필요 없음
        link = anchor['href']  # 링크 따로 저장
        company, kind, region = anchor.find_all('span',
                                                class_='company')  # 세개를 가지고 옴
        # print(company, kind, region)
        title = anchor.find('span', class_='title')
        # print(company, kind, region, title)
        job_data = {
          'link': f"https://weworkremotely.com{link}",
          'company': company.string,
          'location': region.string,
          'position': title.string
        }
        results.append(job_data)
        # print(company.string, kind.string, region.string, title.string)

  return results
