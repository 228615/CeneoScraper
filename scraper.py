import os
import json
import requests
import pandas
import matplotlib
from bs4 import BeautifulSoup

def get_element(ancestor, selector=None, attribute=None, return_list=False):
    try:
        if return_list:
            return [tag.get_text().strip() for tag in ancestor.select(selector)]
        if selector:
            if attribute:
                return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).get_text().strip()
    except (AttributeError, TypeError):
        return None
    if return_list:
        return [tag.get_text().strip() for tag in ancestor.select(selector)]
    if selector:
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).get_text().strip()
    return ancestor[attribute]


single_opinion = {
            "opinion_id": (None, "data-entry-id",), 
            "author": ("span.user-post__author-name",),
            "recommendation": ("span.user-post__author-recomendation > em",),
            "score": ("span.user-post__score-count",),
            "confirmed": ("div.review-pz",),
            "opinion_date": ("span.user-post__published > time:nth-child(1)","datetime",),
            "purchase_date": ("span.user-post__published > time:nth-child(2)","datetime",),
            "up_votes": ("span[id^='votes-yes']",),
            "down_votes": ("span[id^='votes-no']",),
            "content": ("div.user-post__text",),
            "cons": ("div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item", None, True),
            "pros": ("div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item", None, True)
        }



#product_code = input("Podaj kod produktu: ")
product_code = "100361771"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"

while url:
    print(url)
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        page_dom = BeautifulSoup(response.text, "html.parser")
        opinions = page_dom.select("div.js_product-review")
        opinions_all = []

        for opinion in opinions:
            single_opinion = {}
            for key, value in selectors.items():
                single_opinion[key] = get_element(opinion, *value)
            opinions_all.append(single_opinion)
    
        try:
            url = "https://www.ceneo.pl/"+get_element(page_dom, "a.pagination__next", "href")
        except TypeError:
            url = None

if os.path.exists("./opinions"):
    os.mkdir(f"./opinions")
with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(opinions_all, jf, indent=4, ensure_ascii=False)


#print(response.status_code)
