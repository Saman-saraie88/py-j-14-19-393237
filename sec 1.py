

nomre = float(input("nomre ro bego: "))

if nomre < 0 or nomre > 20:
    print("nomre eshtebah ast", "\u00D7")

elif 15 < nomre <= 20:
    print("kheily khoobe", "\u2705")

elif 10 <= nomre <= 15:
    print("bad nist", "\U0001F494")

elif 5 < nomre < 10:
    print("kheily bade", "\U0001F621")

elif 0 <= nomre <= 5:
    print("savad dari?", "\U0001F921")
