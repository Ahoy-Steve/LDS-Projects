list1=[10,13,23,24,21,42]
list1.sort(key=lambda x: x%10)
print(list(list1))


def sort_by_last_digit(numbers):
    # Sortăm lista folosind ultima cifră ca cheie
    return sorted(numbers, key=lambda x: x % 10)

# Exemplu de utilizare
n = input("Introdu lista de numere (separate prin spații): ")
# Transformăm inputul într-o listă de întregi
numbers = list(map(int, n.split()))

# Sortăm lista
sorted_numbers = sort_by_last_digit(numbers)

# Afișăm lista sortată
print("Lista sortată:", sorted_numbers)
