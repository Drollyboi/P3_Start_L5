import schedule
from product_utils import *
import requests
import time

def main():
    def verstuur_notificatie(product):
        bericht = f"nieuw product: {product.titel} en prijs {product.prijs}"
        chatName = "Cheese"
        print(bericht)

    producten = haal_producten_op_simulatie()

    oude_producten = laad_oude_producten()

    print(f"vorige keer waren er {len(oude_producten)} producten")
    print(f"deze keer zijn het er {len(producten)}")

    for product in producten:
        if product not in  oude_producten:
            verstuur_notificatie(product)

schedule.every(10).seconds.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
