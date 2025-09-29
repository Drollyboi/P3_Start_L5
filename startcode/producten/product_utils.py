import requests
from bs4 import BeautifulSoup
from product import Product
import pickle
import random

def laad_oude_producten():
    try:
        with open("producten.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []


def bewaar_producten(producten):
    with open("producten.pkl", "wb") as f:
        pickle.dump(producten, f)


def haal_producten_op():
    basis_url = "https://shop.codefever.rocks/collections/all"
    producten = []

    for page_num in range(1, 3):
        response = requests.get(basis_url, params={"page": page_num})
        soup = BeautifulSoup(response.text, "html.parser")
        for card in soup.select("li.grid__item"):
            link_element = card.select_one("a")
            titel = link_element.text.strip()
            href = link_element["href"].strip()
            link = "https://shop.codefever.rocks" + href
            prijs_element = card.select_one(".price-item--last")
            prijs = prijs_element.text.strip()
            producten.append(Product(titel, link, prijs))

    return producten


def haal_producten_op_simulatie():
    # Haal eerst alle producten op
    producten = haal_producten_op()

    # Geef random aantal producten terug (tussen 80% en 100% van totaal)
    min_producten = int(len(producten) * 0.8)
    aantal = random.randint(min_producten, len(producten))

    # Return random selectie
    return random.sample(producten, aantal)