def total_sold(sales):
    return sum(sales.values())


def most_sold_product(sales):
    return max(sales, key=lambda x: sales[x])


def least_sold_product(sales):
    return min(sales, key=lambda x: sales[x])


def critical_products(sales):
    return [x for x in sales if sales[x] < 50]


def get_product_sales(sales, product):
    try:
        value = sales[product]
        return float(value)

    except KeyError:
        print(f"Greška: proizvod '{product}' ne postoji u prodaji.")
        return None

    except ValueError:
        print(f"Greška: vrijednost za '{product}' nije broj.")
        return None

    except Exception as e:
        print(f"Neočekivana greška: {e}")
        return None


def validate_sales_data(sales):
    """Provjerava negativne i neuobičajeno visoke vrijednosti."""
    try:
        negative_price = [x for x in sales if float(sales[x]) < 0]
        unusual_high_price = [x for x in sales if float(sales[x]) > 100000]

    except Exception as e:
        print(f"Greška pri validaciji podataka: {e}")
        return False

    if negative_price or unusual_high_price:
        print("Pažnja, detektovan je problem u prodaji: negativne ili neuobičajeno visoke vrijednosti!")

        if negative_price:
            print(f"Negativna prodaja: {negative_price}")

        if unusual_high_price:
            print(f"Neuobičajeno visoke vrijednosti prodaje: {unusual_high_price}")

        return False

    else:
        print("Nema nijedan proizvod koji ima negativnu ili neuobičajeno visoke vrijednosti prodaje.")
        return True
   
