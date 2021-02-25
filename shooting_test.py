suma = 0
average = 0
var = 0
var = str(input("variable test: ")) #1 cifras
while True:

    var2 = str(input("variable N: "))
    var = str(var) + str(var2) 
    var = var[1:9]
    print(str(var))
    for char in var:
        suma += int(char)
    average = suma/8
    print("sum: " + str(suma) + ", average: " + str(average))