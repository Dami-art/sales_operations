import sales_operations as so

sales = {
    "Laptop": 15,
    "Mouse": 150,
    "Keyboards": 85,
    "Monitor": 30,
    "USB cables": 200
}


if "Web camera" not in sales:
    sales["Web camera"] = 0


sales["Monitor"] += 5

print(sales)

print("Ukupna količina prodatih proizvoda je:", so.total_sold(sales))
print("Najprodavaniji proizvod je:", so.most_sold_product(sales))
print("Najmanje prodavani proizvod je:", so.least_sold_product(sales))
print("Lista proizvoda sa kritičnom prodajom:", so.critical_products(sales))

print("Prodaja za Laptop:", so.get_product_sales(sales, "Laptop"))

result = so.get_product_sales(sales, "Printer")
if result is not None:
    print("Prodaja za Printer:", result)


print("Izvještaj validacije prodaje:", so.validate_sales_data(sales))