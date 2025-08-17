numb1 = float(input("masukan number pertama : "))
numb2 = float(input("masukan number kedua : "))
operator = input("masukan operator aritmatika (/,-,+,*) : ")

if operator == "+":
    result = numb1+numb2
    print(round(result, 2))

elif operator == "-":
    result = numb1 - numb2
    print(round(result, 2))

elif operator == "*":
    result = numb1 * numb2
    print(round(result, 2))

elif operator == "/":
    result = numb1 / numb2
    print(round(result, 2))
else:
    print("ERROR")