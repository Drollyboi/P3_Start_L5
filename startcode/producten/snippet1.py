from product import Product

product1 = Product("Titel", "www.link.be", "€5,00 EUR")
product2 = Product("Titel", "www.link.be", "€5,00 EUR")

if product1 == product2:
    print("Producten zijn hetzelfde")
else:
    print("Producten zijn verschillend")

