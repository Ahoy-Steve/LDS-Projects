def display(lst):
    if len(lst) >= 1:
        head = lst[0]  # primul element din listă
        tail = lst[1:]  # restul elementelor
        print(head)
        display(tail)  # apel recursiv pentru a afișa restul

# Exemplu de utilizare:
n  = input("pur nr: ")
lst = list(map(int, display(n).split()))
print(f"Sarpele tau e: {lst}")
