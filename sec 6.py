

dama = float(input("dama ra bego: "))

if dama < 0:
    print("kapshan tanet kon.", "\U0001F976")

elif 0 <= dama <= 10:
    print("lebase garm beposh.", "\U0001F636\u200D\U0001F32B")

elif 11 <= dama <= 25:
    print("hava khoobe", "\U0001F31E")

else:
    print("lebase khonak bepoosh", "\U0001F975")
