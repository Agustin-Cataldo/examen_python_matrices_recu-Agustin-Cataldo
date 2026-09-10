matriz= [[],[],[]]
opcion= int(input("1-Cargar matrices \n 2-Mostrar martriz cargada \n 3-Sumatoria \n 4-Prodcutoria \n 5-Traspuesta\n 6-Salir\n"))
while opcion!= 6:
    if opcion== 1:
        for i in range(3):
            f0= int(input("\nIngrese el numero deseado para la primera fila: "))
            matriz[0].append(f0)
        for i in range(3):
            f1= int(input("\nIngrese el numero deseado para la segunda fila: "))
            matriz[1].append(f1)
        for i in range(3):
            f2= int(input("\nIngrese el numero deseado para la tercera fila: "))
            matriz[2].append(f2)
    eleccion = str(input("Ya hay una matriz Cargada desea remplazarla? (V,F): "))
    if eleccion == "V":
        for fila in range(3):
            for columna in range(3):
                if matriz[fila][columna] != "":
                    matriz[fila][columna]= input("Ingrese el con el que lo numero que quiere remplazar: ")
    if opcion == 2:
        for fila in range(3):
            for columna in range(3):
                print(matriz[fila][columna])
    if opcion == 3:
        resultado= matriz[0][0] + matriz[0][1] + matriz[0][2]
        print("El resultado de la fila 0 es: ", resultado)
        resultado_f1= matriz[1][0] + matriz[1][1] + matriz[1][2]
        print("El resultado de la fila 1 es: ", resultado_f1)
        resultado_f2= matriz[2][0] + matriz[2][1] + matriz[2][2]
        print("El resultado de la fila 2 es: ", resultado_f2)
    if opcion == 4:
        res= matriz[0][0] * matriz[0][1]* matriz[0][2]* matriz[1][0]* matriz[1][1]* matriz[1][2]* matriz[2][0]* matriz[2][1]* matriz[2][2]
    if opcion == 5: 
        print("Matriz transpuesta:")
        for c in range(3):
            fila_transpuesta = []
            for f in range(3):
                fila_transpuesta.append(matriz[f][c])
            print(fila_transpuesta)