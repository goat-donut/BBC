from curses.ascii import isdigit, isalpha
def lvl1(s:str, method:str):
    if method == "upper":
        return s.upper()
    elif method == "lower":
        return s.lower()
    elif method == "capitalize":
        return s.capitalize()
def lvl2(s, method:str):
    if method == "find":
        a = str(input())
        return s.find(a)
    elif method == "replace":
        a = str(input())
        b = str(input())
        return s.replace(a, b)
    elif method == "count":
        a = str(input())
        return s.count(a)
def lvl3(s, method:str):
    if method == "join":
        a = str(input())
        return a.join(s)
    elif method == "split":
        a = str(input())
        return s.split(a)
def lvl4(s, method:str):
    if method == "isdigit":
        return s.isdigit()
    elif method == "isalpha":
        return s.isalpha()
    elif method == "strip":
        a = str(input())
        return s.strip(a)
print("choose lvl")
lvl = str(input())
if lvl == "lvl1":
    print("enter text")
    text = str(input())
    print("methods: upper, lower, capitalize")
    print("choose method")
    method = str(input())
    print(lvl1(text, method))
if lvl == "lvl2":
    print("enter text")
    text = str(input())
    print("methods: find, replace, count")
    print("choose method")
    method = str(input())
    print(lvl2(text, method))
if lvl == "lvl3":
    print("enter text")
    text = str(input())
    print("methods: join, split, join")
    print("choose method")
    method = str(input())
    print(lvl3(text, method))
if lvl == "lvl4":
    print("enter text")
    text = str(input())
    print("methods: isdigit, isalpha, strip")
    print("choose method")
    method = str(input())
    print(lvl4(text, method))



