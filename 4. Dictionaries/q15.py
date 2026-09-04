product_price = {
    "Sugar1kg": 225,
    "Mezan Cooking Oil 1L": 650,
    "Wheat Flour Atta 10kg": 1820,
    "Daal Chana 500g": 175,
    "National Turmeric Powder 100g": 330,
}

highest_price = 0
highest_product = "" 

for key, val in product_price.items():
    if val > highest_price:
        highest_price = val
        highest_product = key 

print(f"Highest Priced Product: {highest_product}")
print(f"Price: Rs {highest_price}")