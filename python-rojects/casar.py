def cesar(num, side, text):

    cipher = ""

    for c in text:
        if 1072 <= ord(c) <= 1103:
            if side == ">>>":
                if ord(c) + num <= 1103:
                    cipher += chr(ord(c) + num)
                else: 
                    cipher += chr(ord(c) + num - 32)
            elif side == "<<<":
                if ord(c) - num >= 1072:
                    cipher += chr(ord(c) - num)
                else:
                    cipher += chr(ord(c) - num + 32)
        elif 1040 <= ord(c) <= 1071:
            if side == ">>>":
                if ord(c) + num <= 1071:
                    cipher += chr(ord(c) + num)
                else:
                    cipher += chr(ord(c) + num - 32)
            elif side == "<<<":
                if ord(c) - num >= 1040:
                    cipher += chr(ord(c) - num)
                else:
                    cipher += chr(ord(c) - num + 32)
        elif 97 <= ord(c) <= 122:
            if side == ">>>":  
                if ord(c) + num <= 122:
                    cipher += chr(ord(c) + num)
                else:
                    cipher += chr(ord(c) + num - 32)
            elif side == "<<<":
                if ord(c) - num >= 97:
                    cipher += chr(ord(c) - num)
                else:
                    cipher += chr(ord(c) - num + 26)
        elif 65 <= ord(c) <= 90:
            if side == ">>>":
                if ord(c) + num <= 90:
                    cipher += chr(ord(c) + num)
                else:
                    cipher += chr(ord(c) + num - 32)
            elif side == "<<<":
                if ord(c) - num >= 65:
                    cipher += chr(ord(c) - num)
                else:
                    cipher += chr(ord(c) - num + 26)
        else:
            cipher += c
    
    return cipher


print("Напиши текст")
s = input()
print("В какую сторону двигать? Напиши '<<<' или '>>>'")
t = input()
print("Насколько сдвинуть? Укажи шаг (цифрой)")


for i in range(1, 26):
    n = i
    print(i, cesar(n, t, s))
    





