def get_digits(number):
    # """Returnează lista de cifre ale unui număr."""
    return list(map(int, str(abs(number))))  # Folosim map pentru a transforma fiecare caracter în întreg

def filter_digits(digits, condition):
    # """Filtrează cifrele în funcție de o condiție dată."""
    if condition == 'odd':
        return list(filter(lambda digit: digit % 2 != 0, digits))
    elif condition == 'even':
        return list(filter(lambda digit: digit % 2 == 0, digits))
    elif condition == 'less_than_7':
        return list(filter(lambda digit: digit < 7, digits))
    else:
        return digits  # Dacă nu este nicio condiție, returnează toate cifrele

def build_digit_lists(number, condition):
    # """Construiește listele de cifre în ordinea normală și inversă.""" ( # sau """)
    digits = get_digits(number)
    filtered_digits = filter_digits(digits, condition)
    sorted_digits = sorted(filtered_digits)
    return sorted_digits, sorted_digits[::-1]  # Lista inversată

# Exemplu de utilizare
number = int(input("Introduceti un numar: "))
condition = input("Introduceti conditia (odd, even, less_than_7): ")

normal_order, reverse_order = build_digit_lists(number, condition)
print(f"Cifrele în ordinea normală care satisfac condiția '{condition}': {normal_order}")
print(f"Cifrele în ordinea inversă care satisfac condiția '{condition}': {reverse_order}")
