def toplama(x, y):
    return x + y

def çıxma(x, y):
    return x - y

def hasil(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Ədədi sıfıra bölmək olmaz."

# İstifadəçidən nömrələri və əməliyyat növünü alın
sayi1 = float(input("Birinci reqemi girin: "))
sayi2 = float(input("İkinci reqemi girin: "))
hesablama = input("Etmək istədiyiniz hesablamani seçin (+, -, *, /): ")

# Əməliyyatı yerinə yetirin və nəticəni ekrana çap edin
if hesablama == "+":
    netice = toplama(sayi1, sayi2)
elif hesablama == "-":
    netice = çıxma(sayi1, sayi2)
elif hesablama == "*":
    netice = hasil(sayi1, sayi2)
elif hesablama == "/":
    netice = bolme(sayi1, sayi2)
else:
    netice = "Etibarsız əməliyyat"

print("Sonuç:", netice)
