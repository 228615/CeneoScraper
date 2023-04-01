import json
import requests
from bs4b import BeautifulSoup

# product_code = input("Podaj kod produktu: ")
product_code = "85920806"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
if response.status.code == requests.status.codes.ok:
    page_dom = BeautifullSoup(response.text, "html.parser")
    opinions = page_dom.select("div.js_product-review")
    print(len(opinions))
    print(type(opinions))
    opinions_all = []
    for opinion in opinions:
        single_opinion = {
            "opinion_id": opinion.select_one("data-entry-id").get_text().strip(),
            "author": opinion.select_one("span.user-post__author-name").get_text().strip(),
            "recommendation": opinion.select_one("span.user-post__author-recomendation > em").get_text().strip(),
            "score": opinion.select_one("span.user-post__score-count").get_text().strip(),
            "confrimed": opinion.select_one("div.review-pz").get_text().strip(),
            "opinion_date": opinion.select_one("span.user-post__published > time:nth-child(1)["datetime"]").get_text().strip(),
            "purhase_date": opinion.select_one("span.user-post__published > time:nth-child(2)["datetime"]").get_text().strip(),
            "up_votes": opinion.select_one("span[id^="votes-yes"]").get_text().strip(),
            "down_votes": opinion.select_one("span[id^="votes-no"]").get_text().strip(),
            "content": opinion.select_one("div.user-post__text").get_text().strip(),
            "cons": opinion.select("div.review-feature__col:has(\> div.review-feature__title--negatives) > div.review-feature__item")
            "pros": opinion.select("div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item")
        }
    print(json_dumps(single_opinion, indent=4, ensure_ascii=False))

print(response.status_code)

