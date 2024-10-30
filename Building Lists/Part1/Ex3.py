#Nu poti sa sortezi o lista cu mai multe tipuri de date

# list1=[1,"py",True,2.3]
# list1.sort()
# print(list(list1))
# list1.sort(reverse=True)
# print(list(list1))

# #Rezolvare:
# list1 = [1, "py", True, 2.3, False, "hello", 3]
#
# # Separăm elementele în funcție de tip
# integers = [x for x in list1 if isinstance(x, int)]
# reals = [x for x in list1 if isinstance(x, float)]
# strings = [x for x in list1 if isinstance(x, str)]
# booleans = [x for x in list1 if isinstance(x, bool)]
#
# # Sortăm fiecare sublistă
# integers.sort()
# reals.sort()
# strings.sort()
# booleans.sort()

# # Combinăm sublistele
# sorted_list = integers + reals + strings + booleans

# # Afișăm lista sortată ascendent
# print("Sorted list (ascending):", sorted_list)
#
# # Sortăm și combinăm din nou pentru ordinea descendentă
# sorted_list.reverse()  # sau poți folosi sort(reverse=True)
# print("Sorted list (descending):", sorted_list)


list1 = [1, "py", True, 2.3, False, "hello", 3]

# Funcție pentru a sorta lista pe tipuri
def sort_mixed_list(list):
    # Separăm și sortăm lista pe tipuri
    return sorted(
        list,
        key=lambda x: (type(x).__name__, x)  # Sortăm întâi după tip, apoi după valoare
    )

# Sortăm ascendent
sorted_list_asc = sort_mixed_list(list1)
print("Sorted list (ascending):", sorted_list_asc)

# Sortăm descendent
sorted_list_desc = sorted_list_asc[::-1]  # Inversăm lista
print("Sorted list (descending):", sorted_list_desc)


# type(x).__name__: Obține numele tipului pentru fiecare element (de exemplu, 'int', 'str', 'bool', 'float').
# (type(x).__name__, x): Creează un tuple cu două valori: numele tipului și valoarea efectivă a elementului.
# Aceasta înseamnă că sortarea se va face întâi pe baza tipului și apoi, în cazul în care tipurile sunt identice, pe baza valorii.