from pprint import pprint

import requests
from bs4 import BeautifulSoup

keyword = "Sabonete"

url = f"https://lista.mercadolivre.com.br/{keyword}"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    search_result = soup.find_all("div", class_="ui-search-result")

    data = []
    for result in search_result:
        brand = result.find(
            "span", class_="ui-search-item__group__element"
        ).text.strip()
        title = result.find("a", class_="ui-search-link").text
        price = result.find("span", class_="andes-money-amount__fraction").text.strip()
        link = result.find("a", class_="ui-search-link").get("href")

        data.append({"Brand": brand, "Title": title, "Price": price, "Link": link})

        pprint(data)


else:
    print("erro")
