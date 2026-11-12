

num = int(input("adad ro bego: "))

if num < 2:
    print("adad aval nist")

else:
    for i in range(2, num):
        if num % i == 0:
            print("adad aval nist")
            break
    else:
        print("adad aval hast")
