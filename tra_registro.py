productosRegistrados = 0
productosConDescuento = 0
totalCompras = 0
totalPagado = 0

producto = input("Ingrese el nombre del producto (FIN para terminar):")

while(producto != "FIN"):
    cantidad = int(input("Ingrese la cantidad del producto:"))
    precio = float(input("Ingrese le valor unitario del producto:"))

    productosRegistrados += 1

    totalproducto = cantidad * precio
    descuento = 0

    if(totalproducto >= 100000):
        descuento = totalproducto * 0.10
        productosConDescuento += 1

    elif(totalproducto >= 50000):
        descuento = totalproducto * 0.05
        productosConDescuento += 1

    valorFinal = totalproducto - descuento

    print("\n Producto:",producto)
    print("Valor original: $",totalproducto)
    print("Descuento: $",descuento)
    print("Valor a pagar: $",valorFinal)

    totalCompras += totalproducto
    totalPagado += valorFinal

    producto = input("\n Ingrese el nombre de otro producto (FIN para terminar)")
print("\n ---RESUMEN DE LA COMPRA---")
print("Productos registrados:",productosRegistrados)
print("Productos con descuento:",productosConDescuento) 
print("Valor original de las compras: $",totalCompras)
print("Valor final a pagar: $",totalPagado)