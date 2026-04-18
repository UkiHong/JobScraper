import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-back-end-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(
    response.content,
    "html.parser",
)
jobs = soup.find("section", class_="jobs").find_all("li")[0:-1]

all_jobs = []

for job in jobs:
    title = job.find("span", class_="new-listing__header__title__text")
    company = job.find("p", class_="new-listing__company-name")
    region = job.find_all("p", class_="new-listing__categories__category")
    url = job.find("a", class_="listing-link--unlocked")

    job_data = {
        "title": title.get_text() if title else "no title",
        "company": company.get_text() if company else "no company",
        "region": region[-1].get_text() if region else "no region",
        "url": f"https://weworkremotely.com{url['href']}" if url else "no url",
    }

    all_jobs.append(job_data)

print(all_jobs)
