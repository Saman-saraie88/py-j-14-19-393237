

ghad = float(input("ghad ro bego: "))

if ghad <= 0:
    print("ghad eshtebah vared shode")

vazn = float(input("vazn ro bego: "))

if vazn <= 0:
    print("vazn eshtebah vared shode")

bmi = vazn / (ghad * ghad)

print(bmi)

if 18.5 > bmi:
    print("kambode vazn")

elif 18.5 <= bmi <= 25:
    print("vazn monaseb")

elif 25 < bmi <= 30:
    print("ezafe vazn")

else:
    print("chaghi") 
