

while True:

    num1 = float(input("Adad aval: "))

    amalgar = input("kodom ? (+, -, *, /, **): ")

    num2 = float(input("Adad dovom: "))

    if amalgar == "+":
        print("javab: ", num1 + num2)

    elif amalgar == "-":
        print("javab: ", num1 - num2)

    elif amalgar == "*":
        print("javab: ", num1 * num2)

    elif amalgar == "**":
        print("javab: ", num1 ** num2)

    elif amalgar == "/":
        if num2 != 0:
            print("javab: ", num1 / num2)
        else:
            print("emkane taghsim bar sefr nist")

    else:
        print("Amaliat namotabar ast")

    while True:
        dobare = input("edame bedam? (are/na): ")

        if dobare == "na":
            break

        elif dobare == "are":
            break

        else:
            print("faghat are ya na bego")

    if dobare == "na":
        break
