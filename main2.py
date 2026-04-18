import requests
from bs4 import BeautifulSoup


all_jobs = []


def scrape_page(url):

    response = requests.get(url)

    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )
    jobs = soup.find("section", class_="jobs").find_all("li")[0:-1]

    for job in jobs:
        title = job.find("span", class_="new-listing__header__title__text")
        company = job.find("p", class_="new-listing__company-name")
        region = job.find_all("p", class_="new-listing__categories__category")
        url = job.find_all("a", href=True)

        job_data = {
            "title": title.get_text() if title else "no title",
            "company": company.get_text() if company else "no company",
            "region": region[-1].get_text() if region else "no region",
            "url": (
                f"https://weworkremotely.com{url[1]['href']}"
                if len(url) > 1
                else "no url"
            ),
        }

        all_jobs.append(job_data)


response = requests.get("https://weworkremotely.com/top-trending-remote-jobs")

soup = BeautifulSoup(response.content, "html.parser")

buttons = len(soup.find("div", class_="pagination").find_all("span", class_="page"))

for x in range(buttons):
    url = f"https://weworkremotely.com/top-trending-remote-jobs?page={x+1}"
    scrape_page(url)

print(all_jobs)
print(len(all_jobs))
