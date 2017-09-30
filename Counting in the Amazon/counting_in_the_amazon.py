def count_arara(n):
    lst = []
    while n != 0:
        if n % 2 == 0:
            lst.append("adak")
            n -= 2
        if n % 2 == 1:
            lst.append("anane")
            n -= 1
    return " ".join(lst[::-1])
