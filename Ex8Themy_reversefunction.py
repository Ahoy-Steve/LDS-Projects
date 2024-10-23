def my_reverse(s, i=0):
    if len(s) == 0 :
        return s
    else:
        return my_reverse(s[1:])+s[0];
print(my_reverse("abcde"))