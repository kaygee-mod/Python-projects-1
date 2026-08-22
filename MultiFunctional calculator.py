num1 = float(input("Please enter first number"))
num2 = float(input("Please enter second number"))

resulto = num1 + num2
print(round(resulto,2))

resultt = num1 - num2
print(round(resultt,2))

resulte = num1 * num2
print(round(resulte,2))

resultf = num1 / num2
print(round(resultf,2))
if num2 == 0:
    print("error you cant divide number by zer0")
else:
    resultf = num1 / num2
    



resultu = num1 // num2
print(round(resultu,2))

resultv = num1 % num2 
print(round(resultv,2))

print(f"{resulto} {resultt} {resulte} {resultf}")
