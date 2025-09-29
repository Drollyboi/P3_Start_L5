class Product:
    def __init__(self, titel: str, link: str, prijs: str):
        self.titel = titel
        self.link = link
        self.prijs = self.prijs_naar_float(prijs)
        self.categorie = titel.split()[0].lower()  # Eerste woord

    def prijs_naar_float(self, prijs: str) -> float:
        prijs = prijs.replace("€", "").replace("EUR", "")
        prijs = prijs.strip()
        prijs = prijs.replace(",", ".")
        prijs = float(prijs)
        return prijs