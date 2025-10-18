from product import Product
import pytest


def test_gelijk_bij_zelfde_titel_en_link():
    product1 = Product("T-shirt - Robo ASCII (zwart)", "https://shop.codefever.rocks/p/1", "€20,00")
    product2 = Product("T-shirt - Robo ASCII (zwart)", "https://shop.codefever.rocks/p/1", "€25,00")
    # prijs is anders, maar dat maakt niet uit
    assert product1 == product2


def test_niet_gelijk_bij_andere_titel():
    product1 = Product("T-shirt (zwart)", "https://shop.codefever.rocks/p/1", "€20,00")
    product2 = Product("Hoodie (blauw)", "https://shop.codefever.rocks/p/1", "€20,00")
    assert product1 != product2


def test_niet_gelijk_bij_andere_link():
    product1 = Product("Sokken", "https://shop.codefever.rocks/p/1", "€25,00")
    product2 = Product("Sokken", "https://shop.codefever.rocks/p/2", "€25,00")
    assert product1 != product2


def test_zelfde_variabele():
    product = Product("Trui - Raket (blauw)", "https://shop.codefever.rocks/p/3", "€30,00")
    assert product == product


def test_compleet_andere_producten():
    product1 = Product("Drinkfles", "https://shop.codefever.rocks/p/4", "€7,50")
    product2 = Product("Hoodie", "https://shop.codefever.rocks/p/5", "€35,00")
    assert product1 != product2
